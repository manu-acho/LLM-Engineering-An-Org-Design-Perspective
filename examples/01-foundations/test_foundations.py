"""Run beside foundations_lab.py: python3 -m unittest -v test_foundations.py"""

import copy
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import foundations_lab as lab


class LanguageModelChecks(unittest.TestCase):
    def setUp(self):
        self.counts = lab.train(lab.TRAINING_TEXT)

    def test_learned_frequencies_and_normalisation(self):
        result = lab.probabilities(self.counts, "the")
        self.assertAlmostEqual(result["order"], 0.5)
        self.assertAlmostEqual(result["evidence"], 0.25)
        self.assertAlmostEqual(sum(result.values()), 1.0)

    def test_training_data_changes_prediction(self):
        revised = lab.train(lab.TRAINING_TEXT + ["check the evidence"] * 4)
        self.assertGreater(lab.probabilities(revised, "the")["evidence"], 0.5)

    def test_unknown_is_not_a_plausible_answer(self):
        with self.assertRaises(ValueError):
            lab.probabilities(self.counts, "refund")

    def test_empty_training_rejected(self):
        for sentences in [[], [" "]]:
            with self.subTest(sentences=sentences), self.assertRaises(ValueError):
                lab.train(sentences)

    def test_generation_ends_or_reports_length_limit(self):
        self.assertEqual(lab.generate(self.counts),
                         {"text": "check the order", "stop_reason": "end_token"})
        self.assertEqual(lab.generate(self.counts, 2),
                         {"text": "check the", "stop_reason": "length_limit"})

    def test_temperature_changes_sharpness(self):
        cold = lab.probabilities(self.counts, "the", 0.5)
        warm = lab.probabilities(self.counts, "the", 2.0)
        self.assertGreater(cold["order"], warm["order"])

    def test_softmax_stable_and_bad_inputs_rejected(self):
        values = lab.softmax([1000.0, 999.0, 998.0])
        self.assertTrue(all(math.isfinite(x) for x in values))
        self.assertAlmostEqual(sum(values), 1.0)
        for temperature in [0, -1, float("nan"), True]:
            with self.subTest(temperature=temperature), self.assertRaises(ValueError):
                lab.softmax([1, 0], temperature)


class EvidenceChecks(unittest.TestCase):
    def test_brief_preserves_conflict_and_source_status(self):
        brief = lab.build_brief(lab.CASE)
        self.assertEqual([x["quantity"] for x in brief["facts"]], [12, 12, 10])
        self.assertEqual([x["status"] for x in brief["facts"]],
                         ["recorded", "recorded", "reported"])
        self.assertEqual(brief["comparison"]["order_minus_customer_report"], 2)
        self.assertIn("cause_of_difference", brief["unresolved"])

    def test_input_not_changed_by_preparation(self):
        case = copy.deepcopy(lab.CASE)
        lab.build_brief(case)
        self.assertEqual(case, lab.CASE)

    def test_missing_negative_boolean_and_unsupported_units_rejected(self):
        for key, value in [("quantity", -1), ("quantity", True),
                           ("quantity", None), ("source_id", "")]:
            case = copy.deepcopy(lab.CASE)
            case["order"][key] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                lab.build_brief(case)
        case = copy.deepcopy(lab.CASE)
        case["unit"] = "packs"
        with self.assertRaises(ValueError):
            lab.build_brief(case)

    def test_duplicates_and_missing_records_rejected(self):
        case = copy.deepcopy(lab.CASE)
        case["shipment"]["source_id"] = case["order"]["source_id"]
        with self.assertRaises(ValueError):
            lab.build_brief(case)
        del case["shipment"]
        with self.assertRaises(ValueError):
            lab.build_brief(case)

    def test_request_is_serialisable_and_keeps_unresolved_questions(self):
        messages = lab.make_request(lab.build_brief(lab.CASE))
        restored = json.loads(messages[1]["content"])
        self.assertIn("actual_received_quantity", restored["unresolved"])
        self.assertEqual(restored["permitted_output"], "investigation_brief_only")

    def test_cli_works_from_an_unrelated_directory(self):
        script = Path(lab.__file__).resolve()
        with tempfile.TemporaryDirectory() as directory:
            for example in ["model", "brief", "request"]:
                process = subprocess.run([sys.executable, str(script), example],
                                         cwd=directory, capture_output=True,
                                         text=True, check=True)
                self.assertTrue(json.loads(process.stdout))


if __name__ == "__main__":
    unittest.main()
