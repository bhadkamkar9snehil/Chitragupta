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
        self.assertIn(BASE_RUN["RootCause"], params)
        self.assertIn(BASE_RUN["Resolution"], params)
        # No supersede link and no second UPDATE statement for a fresh candidate.
        self.assertIsNone(params[-1])
        self.assertEqual(len(cur.calls), 1)

    def test_update_existing_links_supersedes_both_directions(self):
        cur = FakeCursor(insert_id="ART-NEW-2")
        top_existing = {"ID": "ART-OLD"}
        result = write_curation_action(cur, run=BASE_RUN, disposition="UPDATE_EXISTING", top_existing=top_existing)

        self.assertEqual(result["action"], "UPDATE_EXISTING_WRITTEN")
        self.assertEqual(result["supersedes"], "ART-OLD")
        insert_sql, insert_params = cur.calls[0]
        self.assertIn("ART-OLD", insert_params)
        update_sql, update_params = cur.calls[1]
        self.assertIn("SupersededBySolutionID", update_sql)
        self.assertEqual(update_params, ("ART-NEW-2", "ART-OLD"))

    def test_reuse_existing_only_bumps_usage_never_touches_content(self):
        cur = FakeCursor()
        top_existing = {"ID": "ART-OLD"}
        result = write_curation_action(cur, run=BASE_RUN, disposition="REUSE_EXISTING", top_existing=top_existing)

        self.assertEqual(result["action"], "REUSE_EXISTING_BUMPED")
        sql, params = cur.calls[0]
        self.assertIn("UsageCount = ISNULL(UsageCount, 0) + 1", sql)
        self.assertNotIn("ResolutionSteps", sql)
        self.assertNotIn("RootCause", sql)
        self.assertEqual(params, (BASE_RUN["RunID"], "ART-OLD"))

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

    def test_create_candidate_refuses_to_write_without_verified_root_cause(self):
        cur = FakeCursor()
        run = dict(BASE_RUN, RootCause="")
        result = write_curation_action(cur, run=run, disposition="CREATE_CANDIDATE", top_existing=None)

        self.assertEqual(result["action"], "NONE")
        self.assertEqual(cur.calls, [])


if __name__ == "__main__":
    unittest.main()
