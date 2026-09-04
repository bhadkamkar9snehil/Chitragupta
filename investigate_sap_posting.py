#!/usr/bin/env python3
"""
Investigate SAP posting issue for Heat H88210 - EAF Area
"""

import argparse
import json
import sys
from datetime import datetime

try:
    import pyodbc
except ImportError:
    print("pyodbc not available, installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyodbc"])
    import pyodbc


class HermesL2Client:
    """Thin wrapper around XStudio database for L2 investigation."""
    
    def __init__(self, server=None, username=None, password=None):
        self.server = server or os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204")
        self.username = username or os.environ.get("MSSQL_MCP_USER", "")
        self.password = password or os.environ.get("MSSQL_MCP_PASSWORD", "")
        self.db_helpdesk = "XStudio_Helpdesk"
        self.db_xbatch = "XStudio_Xbatch"
        
    def connect(self):
        """Establish connections to both databases."""
        conn_str_helpdesk = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.server};"
            f"DATABASE={self.db_helpdesk};"
            f"UID={self.username};"
            f"PWD={self.password};"
            f"TrustServerCertificate=Yes"
        )
        
        conn_str_xbatch = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.server};"
            f"DATABASE={self.db_xbatch};"
            f"UID={self.username};"
            f"PWD={self.password};"
            f"TrustServerCertificate=Yes"
        )
        
        self.conn_helpdesk = pyodbc.connect(conn_str_helpdesk, autocommit=True)
        self.conn_xbatch = pyodbc.connect(conn_str_xbatch, autocommit=True)
        
    def execute_query(self, db, query, params=None):
        """Execute a query and return results."""
        conn = getattr(self, f"conn_{db}")
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        rows = cursor.fetchall()
        
        # Get column names
        desc = [col[0] for col in cursor.description] if cursor.description else []
        
        return list(zip(desc, [str(row[0]) for row in rows])) if rows else []
    
    def get_api_transaction_summary(self, api_type):
        """Get API transaction summary for a given API type."""
        query = """
            SELECT DISTINCT TransactionID, APIType, SAPStatus, ErrorMessage
            FROM XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl
            WHERE IS_DELETED = 0
              AND APIType = @APIType
            ORDER BY TransactionID DESC
        """
        return self.execute_query("xbatch", query, {"@APIType": api_type})
    
    def get_sap_posting_for_heat(self, heat_no):
        """Get SAP posting records for a specific heat."""
        query = """
            SELECT TOP (20) 
                ID, WorkOrderNo, HeatNo, SAP_DocumentNo,
                SAP_Status, SAP_Message, IsProcessed, CreatedOn
            FROM XStudio_Xbatch.dbo.SAP_Posting_Tbl
            WHERE HeatNo = @HeatNo
              AND IS_DELETED = 0
            ORDER BY CreatedOn DESC
        """
        return self.execute_query("xbatch", query, {"@HeatNo": heat_no})
    
    def get_work_orders_for_heat(self, heat_no):
        """Get work orders for a specific heat."""
        query = """
            SELECT TOP (20)
                ID, WorkOrderNo, HeatNo, IsProcessed, SAP_DocumentNo
            FROM XStudio_Xbatch.dbo.MES_Work_Order_Tbl
            WHERE HeatNo LIKE @HeatNo + '%'
              AND IS_DELETED = 0
            ORDER BY CreatedOn DESC
        """
        return self.execute_query("xbatch", query, {"@HeatNo": heat_no})
    
    def execute_hermes_sql(self, sql_text, params=None):
        """Execute SQL through Hermes_L2_Execute_SQL_Usp."""
        conn = self.conn_xbatch
        cursor = conn.cursor()
        
        if params:
            cursor.execute(sql_text, params)
        else:
            cursor.execute(sql_text)
            
        rows = cursor.fetchall()
        desc = [col[0] for col in cursor.description] if cursor.description else []
        
        return list(zip(desc, [str(row[0]) for row in rows])) if rows else None
    
    def close(self):
        """Close database connections."""
        if hasattr(self, 'conn_helpdesk'):
            self.conn_helpdesk.close()
        if hasattr(self, 'conn_xbatch'):
            self.conn_xbatch.close()


def main():
    parser = argparse.ArgumentParser(description="Investigate SAP posting issues")
    parser.add_argument("--heat", required=True, help="Heat number to investigate")
    args = parser.parse_args()
    
    print("=" * 70)
    print(f"SAP POSTING INVESTIGATION FOR HEAT: {args.heat.upper()}")
    print("=" * 70)
    
    client = HermesL2Client()
    
    try:
        client.connect()
        
        heat_no = args.heat
        
        # Step 1: Check if there's an API error log for SAP usage decision
        print("\n[Step 1] Checking API Error Log for UsageDecision...")
        api_errors = client.get_api_transaction_summary("UsageDecision")
        
        if api_errors:
            print(f"   Found {len(api_errors)} error records:")
            for row in api_errors[:5]:
                print(f"\n   - TransactionID: {row[0]}")
                print(f"     APIType: {row[1]}")
                print(f"     SAPStatus: {row[2]}")
                print(f"     ErrorMessage: {row[3][:200] if row[3] else 'N/A'}")
        else:
            print("   No UsageDecision errors found in API Error Log.")
        
        # Step 2: Check SAP posting table for this heat
        print("\n[Step 2] Checking SAP_Posting_Tbl for Heat...")
        postings = client.get_sap_posting_for_heat(heat_no)
        
        if postings:
            print(f"   Found {len(postings)} posting records:")
            stuck_count = 0
            for row in postings:
                work_order = row[1] if len(row) > 1 else "N/A"
                heat = row[2] if len(row) > 2 else "N/A"
                doc_no = row[3] if len(row) > 3 else "N/A"
                status = row[4] if len(row) > 4 else "N/A"
                message = row[5] if len(row) > 5 else "N/A"
                processed = row[6] if len(row) > 6 else "N/A"
                
                print(f"\n   Posting Record:")
                print(f"     WorkOrderNo: {work_order}")
                print(f"     HeatNo: {heat}")
                print(f"     SAP_DocumentNo: {doc_no}")
                print(f"     SAP_Status: {status}")
                print(f"     SAP_Message: {message[:100] if message else 'N/A'}")
                
                # Check for stuck posting (no document number or error status)
                if doc_no == "N/A" and status is not None and "Success" not in str(status):
                    stuck_count += 1
        
        if stuck_count > 0:
            print(f"\n   *** WARNING: {stuck_count} posting(s) appear to be stuck (no document generated)")
        
        else:
            print("   No stuck postings detected.")
        
        # Step 3: Check Work Orders for this heat
        print("\n[Step 3] Checking MES_Work_Order_Tbl for Heat...")
        work_orders = client.get_work_orders_for_heat(heat_no)
        
        if work_orders:
            print(f"   Found {len(work_orders)} work order(s):")
            for row in work_orders[:10]:
                wo_id = row[0] if len(row) > 0 else "N/A"
                wo_no = row[1] if len(row) > 1 else "N/A"
                heat = row[2] if len(row) > 2 else "N/A"
                is_processed = row[3] if len(row) > 3 else "N/A"
                doc_no = row[4] if len(row) > 4 else "N/A"
                
                print(f"\n     Work Order: {wo_no} (ID: {wo_id})")
                print(f"       HeatNo: {heat}")
                print(f"       IsProcessed: {is_processed}")
                print(f"       SAP_DocumentNo: {doc_no}")
        
        # Step 4: Try to call the posting procedure to refresh/verify status
        print("\n[Step 4] Attempting to check posting status via SP...")
        try:
            query = """
                SELECT * FROM dbo.Hermes_L2_Get_Ticket_Context_Usp @TicketID = 'CF7E1711-67EB-4BE6-ABB7-659C26345164'
            """
            context = client.execute_hermes_sql(query)
            if context:
                print(f"   Ticket context retrieved successfully")
        except Exception as e:
            print(f"   Note: Could not retrieve ticket context via SP: {e}")
        
        print("\n" + "=" * 70)
        print("INVESTIGATION COMPLETE")
        print("=" * 70)
        
    finally:
        client.close()


if __name__ == "__main__":
    main()
