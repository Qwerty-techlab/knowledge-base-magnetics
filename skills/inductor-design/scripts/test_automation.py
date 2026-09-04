#!/usr/bin/env python3
"""Регрессионные проверки минимального ТЗ и генератора конфигурации."""
from __future__ import annotations

import copy
import unittest

import prepare_config


class AutomationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.example = prepare_config.load_json(
            prepare_config.SKILL_ROOT / "assets" / "tz_input.example.json"
        )
        self.base = prepare_config.load_json(prepare_config.TEMPLATE_CONFIG)

    def test_example_builds_consistent_config(self):
        config = prepare_config.build_design_config(self.example, self.base)
        single = config["single"]["tz"]
        self.assertAlmostEqual(
            single["p_out_nom"], single["u_out_nom"] * single["i_out_nom"]
        )
        self.assertTrue(config["single"]["enabled"])
        self.assertTrue(config["interleaved"]["enabled"])
        self.assertTrue(config["search"]["exhaustive_core_search"])

    def test_output_current_is_converted_to_power(self):
        data = copy.deepcopy(self.example)
        data["load_definition"] = "output_current"
        data.pop("p_out_W")
        data["i_out_A"] = 20.0
        config = prepare_config.build_design_config(data, self.base)
        self.assertAlmostEqual(
            config["single"]["tz"]["p_out_nom"],
            data["u_out_nom_V"] * data["i_out_A"],
        )

    def test_contradictory_power_and_current_are_rejected(self):
        data = copy.deepcopy(self.example)
        data["i_out_A"] = 1.0
        with self.assertRaisesRegex(ValueError, "противоречие нагрузки"):
            prepare_config.validate_minimal_tz(data)

    def test_invalid_parallel_range_is_rejected(self):
        data = copy.deepcopy(self.example)
        data["search"]["parallel_conductors_min"] = 8
        data["search"]["parallel_conductors_max"] = 4
        with self.assertRaisesRegex(ValueError, "parallel_conductors_min"):
            prepare_config.validate_minimal_tz(data)

    def test_non_boost_voltage_ratio_is_rejected(self):
        data = copy.deepcopy(self.example)
        data["u_in_nom_V"] = data["u_out_nom_V"]
        with self.assertRaisesRegex(ValueError, "u_in_nom_V < u_out_nom_V"):
            prepare_config.validate_minimal_tz(data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
