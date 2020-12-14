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
    split = notes[1].split(",")
    modulos = []
    remainders = []
    for position, bus_index in enumerate(split):
        if bus_index == "x":
            continue
        bus_index = int(bus_index)
        modulos.append(bus_index)
        remainders.append(bus_index - position)
    return chinese_remainder(modulos, remainders)


def chinese_remainder(modulos, remainders):
    """List of modulos, then list of remainders"""
    # https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
    # License: https://www.gnu.org/licenses/old-licenses/fdl-1.2.html
    total = 0
    prod = functools.reduce(lambda a, b: a * b, modulos)
    for modulo, remainder in zip(modulos, remainders):
        p = prod // modulo
        total += remainder * mul_inv(p, modulo) * p
    return total % prod


def mul_inv(a, b):
    # https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
    # License: https://www.gnu.org/licenses/old-licenses/fdl-1.2.html
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


if __name__ == "__main__":
    n = [3, 5, 7]
    a = [2, 3, 2]
    print(chinese_remainder(n, a))


def solve_part_2_iterative(notes) -> int:
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
    main("inputs/day13", 4315, 556100168221141)
