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


def parse_data(data: List[str]):
    return data


def solve_part_1(data) -> int:
    return 0


def solve_part_2(data) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/dayXX-test1")
    main("inputs/dayXX")
