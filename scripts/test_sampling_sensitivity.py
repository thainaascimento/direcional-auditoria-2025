#!/usr/bin/env python3
"""Unit tests for the synthetic PT-530 sample-size sensitivity calculations."""
import unittest

from analyze_synthetic_inventory import (
    attribute_margin,
    hypergeometric_detection_probability,
    minimum_n_for_detection,
)


class SamplingSensitivityTests(unittest.TestCase):
    population_size = 500_000

    def test_minimum_size_for_rarest_synthetic_rate_is_exact(self):
        exception_count = 150  # 0.03%: scenario only, not an entity error rate
        n_min = minimum_n_for_detection(self.population_size, exception_count, 0.95)
        self.assertEqual(n_min, 9_886)
        self.assertLess(hypergeometric_detection_probability(self.population_size, exception_count, n_min - 1), 0.95)
        self.assertGreaterEqual(hypergeometric_detection_probability(self.population_size, exception_count, n_min), 0.95)

    def test_detectability_sensitivity_at_old_and_revised_sizes(self):
        exception_count = 150
        self.assertAlmostEqual(
            hypergeometric_detection_probability(self.population_size, exception_count, 1_000),
            0.25943746498172395,
            places=12,
        )
        self.assertAlmostEqual(
            hypergeometric_detection_probability(self.population_size, exception_count, 10_000),
            0.9517260070677064,
            places=12,
        )

    def test_attribute_precision_is_distinct_from_rare_event_detection(self):
        self.assertAlmostEqual(attribute_margin(self.population_size, 384) * 100, 5.0, delta=0.01)
        self.assertAlmostEqual(attribute_margin(self.population_size, 1_000) * 100, 3.10, delta=0.01)
        self.assertAlmostEqual(attribute_margin(self.population_size, 10_000) * 100, 0.97, delta=0.01)

    def test_detection_sample_sizes_for_several_hypothetical_rates(self):
        expected = {200: 7_433, 500: 2_986, 1_250: 1_196, 2_500: 598, 5_000: 298}
        for exception_count, required_n in expected.items():
            with self.subTest(exception_count=exception_count):
                self.assertEqual(minimum_n_for_detection(self.population_size, exception_count, 0.95), required_n)


if __name__ == "__main__":
    unittest.main()
