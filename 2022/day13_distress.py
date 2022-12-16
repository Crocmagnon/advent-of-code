from __future__ import annotations

import ast


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("\n\n")

    data = parse_data(data)
    solution_part_1 = solve_part_1(data)

    print(f"1. Found {solution_part_1}")
    if expected_part_1:
        assert expected_part_1 == solution_part_1

    solution_part_2 = solve_part_2(data)
    print(f"2. Found {solution_part_2}")
    if expected_part_2:
        assert expected_part_2 == solution_part_2


DataType = list[tuple[list, list]]


def parse_data(data: list[str]) -> DataType:
    pairs = []
    for pair in data:
        left, right = pair.split("\n")
        left = ast.literal_eval(left)
        right = ast.literal_eval(right)
        pairs.append((left, right))
    return pairs


def solve_part_1(data: DataType) -> int:
    total = 0
    for index, pair in enumerate(data):
        left, right = pair
        if lower_than(left, right):
            total += index + 1
    return total


def lower_than(left: list, right: list) -> bool | None:
    """True if left is lower than right."""
    for left_item, right_item in zip(left, right):
        if isinstance(left_item, int) and isinstance(right_item, int):
            if left_item < right_item:
                return True
            elif left_item > right_item:
                return False

        elif isinstance(left_item, list) and isinstance(right_item, list):
            if (res := lower_than(left_item, right_item)) is not None:
                return res

        elif isinstance(left_item, int):
            if (res := lower_than([left_item], right_item)) is not None:
                return res

        elif isinstance(right_item, int):
            if (res := lower_than(left_item, [right_item])) is not None:
                return res

    if len(left) == len(right):
        return None
    return len(left) < len(right)


def solve_part_2(data: DataType) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/day13-test1", expected_part_1=13)
    main("inputs/day13", expected_part_1=5503)
