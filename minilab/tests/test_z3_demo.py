"""Solver smoke tests: only after optional dependency is installed."""
import unittest

from minilab.z3_demo import solve_layout


class Z3SmokeTests(unittest.TestCase):
    def test_two_rooms_fit_in_four_by_three(self):
        result = solve_layout(4)
        self.assertEqual(result["status"], "sat")
        self.assertEqual(result["scope"], "2d_integer_rectangles_only")

    def test_three_by_three_cannot_fit_two_2x2_rooms(self):
        result = solve_layout(3)
        self.assertEqual(result["status"], "unsat")
        self.assertTrue(result["unsat_core"])
        self.assertIn("not be unique", result["warning"])

    def test_failed_constraints_are_not_robot_failure(self):
        result = solve_layout(3)
        self.assertNotIn("robot_success", result)


if __name__ == "__main__":
    unittest.main()
