from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Iterator, List


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("\n")

    data = parse_data(data)
    solution_part_1 = solve_part_1(data)

    print(f"1. Found {solution_part_1}")
    if expected_part_1:
        assert expected_part_1 == solution_part_1

    solution_part_2 = solve_part_2(data)
    print(f"2. Found {solution_part_2}")
    if expected_part_2:
        assert expected_part_2 == solution_part_2


def parse_data(data: List[str]) -> Dict[int, int]:
    dct = defaultdict(int)
    for x in map(int, data[0].split(",")):
        dct[x] += 1
    return dct


def solve_part_1(data) -> int:
    for _ in range(80):
        data = _run_day(data)
    return sum(data.values())


def _run_day(data: Dict[int, int]) -> Dict[int, int]:
    new_data = defaultdict(int)
    for k, v in data.items():
        if k == 0:
            new_data[6] += v
            new_data[8] += v
        else:
            new_data[k - 1] += v
    return new_data


def solve_part_2(data) -> int:
    for _ in range(256):
        data = _run_day(data)
    return sum(data.values())


if __name__ == "__main__":
    main("inputs/day06-test1", expected_part_1=5934, expected_part_2=26984457539)
    main("inputs/day06", expected_part_1=345793)
