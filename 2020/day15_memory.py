import functools
import re
from typing import Dict, Iterable, List, Tuple, Union


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        starting_numbers = list(map(int, f.read().strip().split("\n")[0].split(",")))

    counter_part_1 = solve_part_1(starting_numbers)

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    counter_part_2 = solve_part_2(starting_numbers)
    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


SeenTuple = Union[Tuple[int], Tuple[int, int]]
Seen = Dict[int, SeenTuple]


def solve_part_1(starting_numbers):
    return solve(starting_numbers, 2020)


def solve(starting_numbers, limit):
    seen = dict()  # type: Seen
    previous = 0
    for turn, current in enumerate(starting_numbers):
        seen[current] = (turn,)
        previous = current
    previous_first_time = True
    for turn in range(len(starting_numbers), limit):
        if previous_first_time:
            current = 0
        else:
            current = seen[previous][0] - seen[previous][1]
        seen[current] = seen_tuple(seen, current, turn)
        previous = current
        previous_first_time = first_time_seen(seen, previous)
    return previous


def first_time_seen(seen: Seen, previous: int) -> bool:
    return len(seen[previous]) == 1


def seen_tuple(seen: Seen, current: int, turn: int) -> SeenTuple:
    try:
        existing = seen[current]
        return turn, existing[0]
    except KeyError:
        return (turn,)


def solve_part_2(starting_numbers):
    return solve(starting_numbers, 30_000_000)


if __name__ == "__main__":
    main("inputs/day15-test1", 436, 175594)
    main("inputs/day15-test2", 1, 2578)
    main("inputs/day15-test6", 438, 18)
    main("inputs/day15-test7", 1836, 362)
    main("inputs/day15", 595, 1708310)
