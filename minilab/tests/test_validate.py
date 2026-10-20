"""Learning-only unit tests; failures have explicit causes."""
import copy
import unittest

from minilab.validate import analyze, example_world, shared_wall_length


class EnvironmentChecks(unittest.TestCase):
    def setUp(self):
        self.w = example_world()

    def test_success_is_bounded_rule_feasible_not_robot_rollout(self):
        a = analyze(self.w)
        self.assertEqual(a["status"], "rule_feasible")
        self.assertTrue(a["rule_task_feasible"])
        self.assertIn("no_physics_or_control", a["scope"])

    def test_narrow_door_graph_is_still_connected(self):
        self.w["doors"][0]["width_m"] = 0.45
        result = analyze(self.w)
        self.assertTrue(result["topology_connected"])
        self.assertEqual(result["status"], "blocked_geometry")

    def test_locked_door_blocks_rule_execution(self):
        self.w["doors"][0].update({"locked": True, "key": "K"})
        self.assertEqual(analyze(self.w)["status"], "blocked_state")

    def test_key_and_unlock_capability_unblock(self):
        self.w["doors"][0].update({"locked": True, "key": "K"})
        self.w["robot"]["keys"].append("K")
        self.w["robot"]["capabilities"].append("unlock")
        self.assertEqual(analyze(self.w)["status"], "rule_feasible")

    def test_overlapping_rooms_rejected(self):
        self.w["rooms"][1]["box"] = [3, 0, 7, 4]
        self.assertEqual(analyze(self.w)["status"], "invalid_geometry")

    def test_door_without_shared_wall_rejected(self):
        self.w["rooms"][1]["box"] = [5, 0, 9, 4]
        self.assertEqual(analyze(self.w)["status"], "invalid_geometry")

    def test_door_too_wide_for_contact_rejected(self):
        self.w["doors"][0]["width_m"] = 5
        self.assertEqual(analyze(self.w)["status"], "invalid_geometry")

    def test_missing_target_rejected_as_input(self):
        self.w["objects"] = []
        self.assertEqual(analyze(self.w)["status"], "invalid_input")

    def test_missing_grasp_capability(self):
        self.w["robot"]["capabilities"].remove("grasp")
        self.assertEqual(analyze(self.w)["status"], "blocked_action")

    def test_nongraspable_object(self):
        self.w["objects"][0]["graspable"] = False
        self.assertEqual(analyze(self.w)["status"], "blocked_action")

    def test_no_topological_route(self):
        self.w["doors"] = []
        self.assertEqual(analyze(self.w)["status"], "blocked_topology")

    def test_narrow_door_is_not_an_unsat_proof(self):
        self.w["doors"][0]["width_m"] = 0.45
        result = analyze(self.w)
        self.assertNotEqual(result["status"], "invalid_geometry")

    def test_contact_length(self):
        self.assertEqual(shared_wall_length([0, 0, 4, 4], [4, 1, 8, 3]), 2)
        self.assertEqual(shared_wall_length([0, 0, 4, 4], [5, 0, 8, 4]), 0)

    def test_deterministic(self):
        self.assertEqual(analyze(self.w), analyze(copy.deepcopy(self.w)))


if __name__ == "__main__":
    unittest.main()
