from collections.abc import Generator
from typing import TypeVar


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


DataType = str
T = TypeVar("T")


def parse_data(data: list[str]) -> DataType:
    return data[0]


def solve_part_1(data: DataType) -> int:
    size = 4
    for index, window in enumerate(sliding_window(data, size)):
        if not repeating(window):
            return index + size
    return 0


def repeating(chars: str) -> bool:
    return len(set(chars)) != len(chars)


def sliding_window(stream: str, size: int) -> Generator[str]:
    for i in range(len(stream) - size):
        yield stream[i : i + size]


def solve_part_2(data: DataType) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/day06-test1", expected_part_1=10)
    main("inputs/day06", expected_part_1=1578)
