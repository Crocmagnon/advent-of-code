from __future__ import annotations

import dataclasses
import re


def main(filename: str, expected_part_1: str = None, expected_part_2: str = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().rstrip().split("\n\n")

    data = parse_data(data)
    solution_part_1 = solve_part_1(data)

    print(f"1. Found {solution_part_1}")
    if expected_part_1:
        assert expected_part_1 == solution_part_1

    solution_part_2 = solve_part_2(data)
    print(f"2. Found {solution_part_2}")
    if expected_part_2:
        assert expected_part_2 == solution_part_2


@dataclasses.dataclass
class Instruction:
    quantity: int
    source: int
    destination: int

    @classmethod
    def from_text(cls, text) -> Instruction:
        match = re.match(r"move (\d) from (\d) to (\d)", text)
        quantity, source, destination = match.groups()
        return cls(quantity, source, destination)


@dataclasses.dataclass
class Game:
    stacks: list[list[str]]
    instructions: list[Instruction]


DataType = Game


def parse_data(data: list[str]) -> DataType:
    stacks, instructions = data
    parsed_instructions = []
    for instruction in instructions.split("\n"):
        parsed_instructions.append(Instruction.from_text(instruction))
    print(stacks.split("\n"))
    return None


def solve_part_1(data: DataType) -> str:
    return "0"


def solve_part_2(data: DataType) -> str:
    return "0"


if __name__ == "__main__":
    main("inputs/day05-test1", expected_part_1="CMZ")
    main("inputs/day05")
