"""Optional independent Z3 learning example: rectangle layout satisfiability.

Not the Einstein Layout implementation, and definitely not robot execution.
Run after: python -m pip install -r minilab/requirements.txt
"""
from __future__ import annotations

import argparse
import json


def solve_layout(building_width: int) -> dict:
    from z3 import And, Int, Or, Solver, sat, unsat

    s = Solver()
    x_a, y_a, x_b, y_b = Int("x_a"), Int("y_a"), Int("x_b"), Int("y_b")
    labels = {
        "a_inside": And(x_a >= 0, y_a >= 0, x_a + 2 <= building_width, y_a + 2 <= 3),
        "b_inside": And(x_b >= 0, y_b >= 0, x_b + 2 <= building_width, y_b + 2 <= 3),
        "no_overlap": Or(x_a + 2 <= x_b, x_b + 2 <= x_a,
                         y_a + 2 <= y_b, y_b + 2 <= y_a),
    }
    for name, constraint in labels.items():
        s.assert_and_track(constraint, name)
    status = s.check()
    if status == sat:
        model = s.model()
        return {"status": "sat", "model": {str(v): model[v].as_long()
                                           for v in (x_a, y_a, x_b, y_b)},
                "scope": "2d_integer_rectangles_only"}
    if status == unsat:
        return {"status": "unsat",
                "unsat_core": [str(k) for k in s.unsat_core()],
                "warning": "A core need not be unique or minimum"}
    return {"status": "unknown", "reason": s.reason_unknown()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=None,
                        help="Width of toy building; default compare widths 4 and 3")
    args = parser.parse_args()
    widths = [args.width] if args.width is not None else [4, 3]
    for width in widths:
        print(json.dumps({"building_width": width, **solve_layout(width)},
                         indent=2, ensure_ascii=False))
