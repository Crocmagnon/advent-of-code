import copy
import functools
import itertools
from typing import List, Tuple

import networkx as nx


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        jolts = sorted(map(int, f.read().strip().split("\n")))  # type: List[int]

    jolts.append(jolts[-1] + 3)

    counter_part_1 = solve_part_1(jolts)
    jolts.insert(0, 0)
    counter_part_2 = solve_part_2(jolts)

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


def solve_part_2(jolts: List[int]):
    jolts = tuple(jolts)
    return with_recursion(jolts, jolts[-1])


@functools.lru_cache(maxsize=None)
def with_recursion(jolts: Tuple[int], target: int):
    if target == 0:
        return 1
    counter = 0
    for jolt in jolts:
        if can_reach(jolt, target):
            counter += with_recursion(jolts, jolt)
    return counter


def can_reach(jolt, target):
    return 0 < target - jolt < 4


def with_graph(jolts):
    """
    It works but it's way too slow for the real deal.
    """
    graph = nx.DiGraph()
    combinations = itertools.combinations(jolts, 2)
    for combination in combinations:
        combination = sorted(combination)
        diff = combination[1] - combination[0]
        if 0 < diff < 4:
            graph.add_edge(combination[0], combination[1])
    paths_counter = 0
    for _ in nx.all_simple_paths(graph, jolts[0], jolts[-1]):
        paths_counter += 1
    return paths_counter


if __name__ == "__main__":
    main("inputs/day10-test1", 35, 8)
    main("inputs/day10-test2", 220, 19208)
    main("inputs/day10", 2450)
