import enum
import functools
import math
from typing import List, Dict


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        notes = f.read().strip().split("\n")

    counter_part_1 = solve_part_1(notes)

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    counter_part_2 = solve_part_2(notes)
    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


def solve_part_1(notes) -> int:
    earliest = int(notes[0])
    buses = map(int, filter(lambda bus: bus != "x", notes[1].split(",")))
    min_delta = math.inf
    min_bus = None
    for bus in buses:
        delta = math.ceil(earliest / bus) * bus - earliest
        if delta < min_delta:
            min_delta = delta
            min_bus = bus

    return min_bus * min_delta


def solve_part_2(notes) -> int:
    """Works but far too slow for the real deal."""
    split = notes[1].split(",")
    buses = list(map(int, filter(lambda bus: bus != "x", split)))
    minutes = {}  # type: Dict[int, int]
    biggest_bus = max(buses)
    biggest_bus_index = split.index(str(biggest_bus))

    for bus in buses:
        minutes[split.index(str(bus)) - biggest_bus_index] = bus

    found = False
    timestamp = 99999999999628
    while not found:
        timestamp += biggest_bus
        found = True
        for delta, bus in minutes.items():
            if (timestamp + delta) % bus != 0:
                found = False
                break

    return timestamp + min(minutes.keys())


if __name__ == "__main__":
    main("inputs/day13-test1", 295, 1068781)
    main("inputs/day13-test2", None, 3417)
    main("inputs/day13-test3", None, 754018)
    main("inputs/day13-test4", None, 779210)
    main("inputs/day13-test5", None, 1261476)
    main("inputs/day13-test6", None, 1202161486)
    main("inputs/day13", 4315)
