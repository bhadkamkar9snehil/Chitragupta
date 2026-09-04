#!/usr/bin/env python3
"""Publish QUESTION response for blocked ticket via raw MSSQL connection."""

import os
import pyodbc

# Load credentials (assumes standard env vars or .env in project)
try:
    server = os.getenv("MSSQL_MCP_SERVER", "10.2.6.204")
    database = "XStudio_Helpdesk"
    
    # Try with different connection string approaches
    conn_str = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};TrustServerCertificate=Yes"
    
    conn = pyodbc.connect(conn_str)
    print("Connected successfully!")
except ImportError:
    print("pyodbc not installed - cannot connect to database")
    print("This environment needs: pip install pyodbc or ensure sqlcmd is accessible")
