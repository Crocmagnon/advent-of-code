import math
import statistics
from typing import List


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


def parse_data(data: List[str]) -> List[int]:
    return list(map(int, data[0].split(",")))


def solve_part_1(data: List[int]) -> int:
    target_position = int(statistics.median(data))
    fuel_cost = 0
    for crab in data:
        fuel_cost += abs(crab - target_position)
    return fuel_cost


def solve_part_2(data: List[int]) -> int:
    target_position_1 = math.floor(statistics.mean(data))
    target_position_2 = math.ceil(statistics.mean(data))
    return min(
        [
            compute_part_2(data, target_position_1),
            compute_part_2(data, target_position_2),
        ]
    )


def compute_part_2(data: List[int], target_position: int) -> int:
    fuel_cost = 0
    for index, crab in enumerate(data):
        fuel_for_crab = sum([i for i in range(abs(crab - target_position) + 1)])
        fuel_cost += fuel_for_crab
    return fuel_cost


if __name__ == "__main__":
    main("inputs/day07-test1", expected_part_1=37, expected_part_2=168)
    main("inputs/day07", expected_part_1=349769, expected_part_2=99540554)
