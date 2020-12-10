import copy
import itertools
from typing import List


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        jolts = sorted(map(int, f.read().strip().split("\n")))  # type: List[int]

    jolts.append(jolts[-1] + 3)

    counter_part_1 = solve_part_1(jolts)
    counter_part_2 = 0

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


def solve_part_1(jolts):
    diffs = count_diffs(jolts)
    return diffs[1] * diffs[3]


def count_diffs(jolts):
    diffs = {1: 0, 2: 0, 3: 0}
    previous = 0
    for jolt in jolts:
        diffs[jolt - previous] += 1
        previous = jolt
    return diffs


if __name__ == "__main__":
    main("inputs/day10-test1", 35, 8)
    main("inputs/day10-test2", 220, 19208)
    main("inputs/day10", 2450)
