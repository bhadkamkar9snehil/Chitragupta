"""No-Qwen fact extraction and templated replies, on text/rows from real seeded tickets."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import direct_answer as d  # noqa: E402


def _probe(table, column, value, rows, action_id="A1"):
    return {"probe": {"ok": True, "probe_possible": True, "table": table, "action_id": action_id,
                      "identifier": {"column": column, "value": value}, "rows": rows}}


class ReportedValueTests(unittest.TestCase):
    def test_value_after_connector_word(self):
        text = "Operator logged ArcingTime of 21.0000 min for Heat 1604007. PowerONTime (24.0000)"
        self.assertEqual(d.reported_value(text, "ArcingTime"), "21.0000")
        self.assertEqual(d.reported_value(text, "PowerONTime"), "24.0000")

    def test_prose_between_name_and_number_is_not_a_value(self):
        # Ticket_338 title: the heat number is not the reported arcing time.
        self.assertIsNone(d.reported_value("LRF Arcing time inquiry for Heat 1604007", "ArcingTime"))

    def test_identifier_words_and_element_aliases(self):
        text = "chemistry for Heat 1604014 (Grade HHMNB500B, SampleType F1) showing Carbon=0.0700"
        self.assertEqual(d.reported_value(text, "Grade"), "HHMNB500B")
        self.assertEqual(d.reported_value(text, "SampleType"), "F1")
        self.assertEqual(d.reported_value(text, "C"), "0.0700")


class FactTableTests(unittest.TestCase):
    def test_minutes_seconds_compare_as_durations(self):
        ticket = {"Description": "Shift log shows PowerOnTime of 50:5 and PowerOffTime of 11:47"}
        facts = d.build_facts(ticket, [_probe("dbo.EAF_PER_HEAT", "HeatID", "1604007",
                                              [{"PowerOnTime": "50:05", "PowerOffTime": "11:48"}])])
        by_field = {f["field"]: f["matches"] for f in facts["facts"]}
        self.assertEqual(by_field, {"PowerOnTime": True, "PowerOffTime": False})

    def test_best_row_is_the_one_the_ticket_names(self):
        ticket = {"Description": "Confirm Billet 1604014_S1_29 CutStartTime 2026-07-08 19:08:54.127"}
        rows = [{"BilletNo": "1604014_S2_30", "CutStartTime": "2026-07-08 18:45:55.923"},
                {"BilletNo": "1604014_S1_29", "CutStartTime": "2026-07-08 19:08:54.127000"}]
        facts = d.build_facts(ticket, [_probe("dbo.XMES", "HeatNo", "1604014", rows)])
        self.assertEqual(facts["mismatches"], 0)
        self.assertEqual(facts["compared"], 1)  # CutStartTime; "Billet" alone does not name BilletNo

    def test_phrase_names_a_column_suffix(self):
        ticket = {"BriefDetails": "Material Document 5003509895 posting status"}
        facts = d.build_facts(ticket, [_probe("dbo.MES", "MaterialDocument", "5003509895",
                                              [{"SAPPostingStatus": "Posted", "Plant": "P1"}])])
        self.assertEqual([f["field"] for f in facts["facts"]], ["SAPPostingStatus"])

    def test_probe_without_action_id_cannot_become_a_fact(self):
        ticket = {"Description": "ArcingTime of 21"}
        facts = d.build_facts(ticket, [_probe("dbo.LRF", "HeatID", "1", [{"ArcingTime": 21}], action_id=None)])
        self.assertEqual(facts["facts"], [])


class ProposalTests(unittest.TestCase):
    TICKET = {"BriefDetails": "LRF Arcing time inquiry", "Description": "ArcingTime of 21.0000 min"}

    def _table(self, recorded):
        return d.build_facts(self.TICKET, [_probe("dbo.LRF_Per_Heat", "HeatID", "1604007",
                                                  [{"ArcingTime": recorded}])])

    def test_confirmed_resolution_cites_every_fact(self):
        p = d.proposal_for("CONFIRMED", self._table("21.0000"), run_id="r", ticket_id="t", ticket=self.TICKET)
        self.assertEqual(p["response_type"], "RESOLUTION")
        self.assertIn("match what you reported", p["reply_text"])
        self.assertEqual(p["claims"][0]["evidence"], [{"action_id": "A1"}])
        self.assertEqual(p["claims"][0]["status"], "VERIFIED")

    def test_outcome_the_facts_contradict_is_refused(self):
        self.assertIsNone(d.proposal_for("CONFIRMED", self._table("22"), run_id="r", ticket_id="t",
                                         ticket=self.TICKET))
        self.assertIsNone(d.proposal_for("NEEDS_REASONING", self._table("21"), run_id="r", ticket_id="t",
                                         ticket=self.TICKET))

    def test_not_found_asks_the_requester(self):
        table = d.build_facts(self.TICKET, [_probe("dbo.LRF_Per_Heat", "HeatID", "9", [])])
        p = d.proposal_for("NOT_FOUND", table, run_id="r", ticket_id="t", ticket=self.TICKET)
        self.assertEqual(p["response_type"], "QUESTION")
        self.assertIn("HeatID 9", p["reply_text"])


if __name__ == "__main__":
    unittest.main()
