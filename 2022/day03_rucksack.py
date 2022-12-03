from typing import List, Tuple
import string


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


DataType = List[Tuple[str, str]]


def parse_data(data: List[str]) -> DataType:
    sacks = []
    for line in data:
        stop = int(len(line) /2)
        halves = (line[:stop], line[stop:])
        sacks.append(halves)
    return sacks


def solve_part_1(data: DataType) -> int:
    total = 0
    for halves in data:
        first_half, second_half = set(halves[0]), set(halves[1])
        common_letter = first_half.intersection(second_half).pop()
        total += string.ascii_letters.index(common_letter) + 1
    return total


def solve_part_2(data: DataType) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/day03-test1", expected_part_1=157)
    main("inputs/day03", expected_part_1=7716)
