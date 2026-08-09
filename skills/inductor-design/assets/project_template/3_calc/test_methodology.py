# -*- coding: utf-8 -*-
"""Параметрические проверки исправленной расчётной методики."""
from __future__ import annotations

import json
import math
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "5_interleaved"))

import inductor_design as ind
import interleaved_design as inter


class MethodologyTests(unittest.TestCase):
    def test_volt_second_balance_for_configured_modes(self):
        for tz in (ind.load_tz(), inter.load_tz3().phase_tz()):
            for frequency in tz.f_sw_list:
                mode = ind.compute_mode(tz, frequency)
                expected = 1.0 - tz.u_in_nom / tz.u_out_nom
                self.assertAlmostEqual(mode.D, expected, places=14)
                for case in mode.cases:
                    self.assertLess(abs(case["volt_second_V"]), 1e-9)

    def test_igse_normalization_reproduces_steinmetz_for_sine(self):
        mat = next(iter(ind.material_library().values()))
        frequency, b_peak, count = 100e3, 0.1, 50000
        step = 2.0 * math.pi / count
        integral = sum(abs(math.cos((index + 0.5) * step)) ** mat.alpha
                       for index in range(count)) * step
        p_igse = (ind.igse_ki(mat) * (2.0 * math.pi * frequency * b_peak) ** mat.alpha
                  * (2.0 * b_peak) ** (mat.beta - mat.alpha)
                  * integral / (2.0 * math.pi))
        p_steinmetz = mat.k_st * frequency ** mat.alpha * b_peak ** mat.beta
        self.assertAlmostEqual(p_igse / p_steinmetz, 1.0, places=5)

    def test_gap_uses_physical_area_and_inverts_al(self):
        checked = 0
        materials = ind.material_library()
        for core in ind.core_library().values():
            if core.A_g is None:
                continue
            material = next((name for name in materials
                             if core.A_L0_of(name) > 0.0), None)
            if material is None:
                continue
            al = 0.25 * core.A_L0_of(material)
            gap, _factor, _iterations = ind.gap_for_AL(
                al, core, 0.90, A_L0=core.A_L0_of(material))
            restored = ind.AL_from_gap(
                gap, core, 0.90, A_L0=core.A_L0_of(material))
            self.assertLess(abs(restored / al - 1.0), 1e-3)
            checked += 1
        self.assertGreater(checked, 0)

    def test_inductance_tolerance_is_not_cancelled(self):
        for tz in (ind.load_tz(), inter.load_tz3().phase_tz()):
            for frequency in tz.f_sw_list:
                mode = ind.compute_mode(tz, frequency)
                target = mode.L_req / (1.0 - tz.tol_L)
                self.assertGreaterEqual(target, mode.L_req)
                self.assertAlmostEqual(
                    target * (1.0 - tz.tol_L), mode.L_req, places=12)

    def test_effective_frequency_uses_total_rms_current(self):
        for tz in (ind.load_tz(), inter.load_tz3().phase_tz()):
            for frequency in tz.f_sw_list:
                mode = ind.compute_mode(tz, frequency)
                period = 1.0 / mode.f_sw
                slope_on = mode.dI_pp / (mode.D * period)
                slope_off = mode.dI_pp / ((1.0 - mode.D) * period)
                slope_rms = math.sqrt(
                    mode.D * slope_on ** 2
                    + (1.0 - mode.D) * slope_off ** 2)
                expected = slope_rms / (2.0 * math.pi * mode.I_rms)
                self.assertAlmostEqual(mode.f_eff, expected, places=12)

    def test_missing_core_material_is_not_silently_substituted(self):
        materials = ind.material_library()
        checked = 0
        for core in ind.core_library().values():
            supported = [name for name in materials if core.A_L0_of(name) > 0.0]
            unsupported = [name for name in materials if core.A_L0_of(name) == 0.0]
            if not supported or not unsupported:
                continue
            self.assertGreater(core.A_L0_of(supported[0]), 0.0)
            self.assertEqual(core.A_L0_of(unsupported[0]), 0.0)
            checked += 1
        self.assertGreater(checked, 0)

    def test_interleaved_ripple_formula_matches_numeric_sum(self):
        n_phases = inter.load_tz3().n_phases
        for duty in (0.21, 0.32, 0.415, 0.72):
            analytic = inter.ripple_cancellation_factor(duty, n_phases)
            numeric = inter.ripple_cancellation_numeric(duty, n_phases, 30000)
            self.assertLess(abs(analytic - numeric), 2e-4)

    def test_single_results_follow_configured_limits_and_quantities(self):
        path = os.path.join(HERE, "results_single_gap.json")
        if not os.path.isfile(path):
            self.skipTest("сначала выполнить inductor_design.py")
        with open(path, encoding="utf-8") as stream:
            payload = json.load(stream)
        limit = payload["tz"]["j_final_max"] / 1e6
        for result in payload["results"].values():
            self.assertEqual(result["quantities"]["core_sets"], 1)
            self.assertEqual(result["quantities"]["core_halves_total"], 2)
            selected = result["selected"]
            self.assertLessEqual(selected["design"]["current_density_A_mm2"], limit)
            self.assertEqual(selected["design"]["n_gaps"], 1)
            fallback = result["selection"]["fallback_E_used"]
            self.assertEqual(selected["core"]["family"] == "E", fallback)
            self.assertFalse(selected["verification"]["final_verified"])
            self.assertIsNone(selected["margins"]["L_diff"]["ok"])
            self.assertIsNone(selected["margins"]["B_fem"]["ok"])

    def test_interleaved_results_follow_phase_quantities(self):
        path = os.path.join(ROOT, "5_interleaved", "results_interleaved.json")
        if not os.path.isfile(path):
            self.skipTest("сначала выполнить interleaved_design.py")
        with open(path, encoding="utf-8") as stream:
            payload = json.load(stream)
        phases = payload["tz"]["n_phases"]
        for result in payload["results"].values():
            quantities = result["quantities"]
            self.assertEqual(quantities["phase_inductors"], phases)
            self.assertEqual(quantities["core_sets_total"], phases)
            self.assertEqual(quantities["core_halves_total"], 2 * phases)
            selected = result["selected"]
            self.assertAlmostEqual(
                selected["losses"]["P_total_system_W"],
                phases * selected["losses"]["P_total_W"], places=10)
            self.assertFalse(selected["verification"]["final_verified"])
            self.assertIsNone(selected["margins"]["L_diff"]["ok"])
            self.assertIsNone(selected["margins"]["B_fem"]["ok"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
