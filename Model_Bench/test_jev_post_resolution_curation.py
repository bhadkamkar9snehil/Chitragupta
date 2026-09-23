import unittest

from Model_Bench.jev_post_resolution_curation import write_curation_action


class FakeCursor:
    """Minimal pyodbc-cursor stand-in: records every statement, and
    execute() returns self so .fetchone() chains the way pyodbc's does.
    """

    def __init__(self, insert_id="NEW-ID-1"):
        self.calls: list[tuple[str, tuple]] = []
        self._insert_id = insert_id

    def execute(self, sql, *params):
        self.calls.append((sql, params))
        return self

    def fetchone(self):
        return (self._insert_id,)


BASE_RUN = {
    "RunID": "RUN-1",
    "TicketID": "TICKET-1",
    "TicketNo": "Ticket_500",
    "Route": "heat_execution",
    "ProblemSummary": "EAF power draw looked abnormal for Heat 123.",
    "RootCause": "Transformer tap setting was left at the wrong stage after maintenance.",
    "Resolution": "Reset transformer tap to the documented stage; verified live reading matched spec.",
}


class WriteCurationActionTests(unittest.TestCase):
    def test_create_candidate_inserts_a_new_candidate_row(self):
        cur = FakeCursor(insert_id="ART-NEW")
        result = write_curation_action(cur, run=BASE_RUN, disposition="CREATE_CANDIDATE", top_existing=None)

        self.assertEqual(result["action"], "CREATE_CANDIDATE_WRITTEN")
        self.assertEqual(result["article_id"], "ART-NEW")
        insert_sql, params = cur.calls[0]
        self.assertIn("INSERT INTO dbo.Hermes_Solution_Article_Mst_Tbl", insert_sql)
        self.assertIn("'Candidate'", insert_sql)
        # The article table carries a trigger; a bare OUTPUT clause fails there (SQL error 334).
        self.assertIn("OUTPUT INSERTED.ID INTO @ids", insert_sql)
        self.assertIn(BASE_RUN["RootCause"], params)
        self.assertIn(BASE_RUN["Resolution"], params)
        # No supersede link and no second UPDATE statement for a fresh candidate.
        self.assertIsNone(params[-2])
        self.assertEqual(len(cur.calls), 1)

    def test_verified_resolution_without_root_cause_still_becomes_a_candidate(self):
        """Live: every RESOLUTION lacked RootCause, so no article was ever written."""
        run = {**BASE_RUN, "RootCause": None}
        cur = FakeCursor(insert_id="ART-VERIFY")
        result = write_curation_action(cur, run=run, disposition="CREATE_CANDIDATE", top_existing=None)
        self.assertEqual(result["action"], "CREATE_CANDIDATE_WRITTEN")
        self.assertIn("'Candidate'", cur.calls[0][0])
        self.assertEqual(cur.calls[0][1][-1], "HowTo")

    def test_knowledge_type_satisfies_the_live_check_constraint(self):
        """CK_Hermes_Solution_KnowledgeType: HowTo / Diagnostic / KnownIssue only."""
        cur = FakeCursor()
        write_curation_action(cur, run=BASE_RUN, disposition="CREATE_CANDIDATE", top_existing=None)
        self.assertEqual(cur.calls[0][1][-1], "KnownIssue")

    def test_title_fits_the_varchar_100_column(self):
        run = {**BASE_RUN, "ProblemSummary": "x" * 400}
        cur = FakeCursor()
        write_curation_action(cur, run=run, disposition="CREATE_CANDIDATE", top_existing=None)
        self.assertLessEqual(len(cur.calls[0][1][0]), 100)

    def test_no_article_without_a_verified_resolution(self):
        run = {**BASE_RUN, "Resolution": ""}
        result = write_curation_action(FakeCursor(insert_id="X"), run=run, disposition="CREATE_CANDIDATE", top_existing=None)
        self.assertEqual(result["action"], "NONE")

    def test_update_existing_creates_replacement_candidate_without_retiring_predecessor(self):
        cur = FakeCursor(insert_id="ART-NEW-2")
        top_existing = {"ID": "ART-OLD"}
        result = write_curation_action(cur, run=BASE_RUN, disposition="UPDATE_EXISTING", top_existing=top_existing)

        self.assertEqual(result["action"], "UPDATE_EXISTING_WRITTEN")
        self.assertEqual(result["supersedes"], "ART-OLD")
        insert_sql, insert_params = cur.calls[0]
        self.assertIn("ART-OLD", insert_params)
        self.assertIn("'Candidate'", insert_sql)
        # The predecessor remains Approved/retrievable until the replacement earns
        # independent corroboration; no second UPDATE is allowed at creation time.
        self.assertEqual(len(cur.calls), 1)

    def test_reuse_existing_uses_the_single_link_owner_then_promotes(self):
        cur = FakeCursor()
        top_existing = {"ID": "ART-OLD"}
        result = write_curation_action(cur, run=BASE_RUN, disposition="REUSE_EXISTING", top_existing=top_existing)

        self.assertEqual(result["action"], "REUSE_EXISTING_LINKED")
        link_sql, link_params = cur.calls[0]
        self.assertIn("Hermes_Link_Solution_To_Ticket_Usp", link_sql)
        self.assertNotIn("UsageCount =", link_sql)
        self.assertEqual(
            link_params,
            (BASE_RUN["TicketID"], "ART-OLD", BASE_RUN["RunID"]),
        )

        promote_sql, promote_params = cur.calls[1]
        self.assertIn("ArticleStatus = 'Approved'", promote_sql)
        self.assertIn("ArticleStatus = 'Candidate'", promote_sql)
        self.assertIn("SourceTicketID", promote_sql)
        self.assertIn("ArticleStatus = 'Superseded'", promote_sql)
        self.assertIn("SupersededBySolutionID", promote_sql)
        self.assertIn("SupersedesSolutionID", promote_sql)
        self.assertEqual(promote_params, ("ART-OLD", BASE_RUN["TicketID"]))

    def test_replacement_is_retired_only_inside_successful_promotion_statement(self):
        cur = FakeCursor()
        write_curation_action(
            cur,
            run=BASE_RUN,
            disposition="REUSE_EXISTING",
            top_existing={"ID": "ART-NEW"},
        )

        promote_sql = cur.calls[1][0]
        self.assertIn("OUTPUT INSERTED.ID, INSERTED.SupersedesSolutionID", promote_sql)
        self.assertIn("INNER JOIN @promoted", promote_sql)
        self.assertIn("previous.ArticleStatus = 'Superseded'", promote_sql)
        self.assertIn("previous.IsActive = 0", promote_sql)

    def test_reuse_existing_without_a_candidate_is_a_noop(self):
        cur = FakeCursor()
        result = write_curation_action(cur, run=BASE_RUN, disposition="REUSE_EXISTING", top_existing=None)

        self.assertEqual(result["action"], "NONE")
        self.assertEqual(cur.calls, [])

    def test_none_disposition_writes_nothing(self):
        cur = FakeCursor()
        result = write_curation_action(cur, run=BASE_RUN, disposition="NONE", top_existing=None)

        self.assertEqual(result["action"], "NONE")
        self.assertEqual(cur.calls, [])

if __name__ == "__main__":
    unittest.main()
