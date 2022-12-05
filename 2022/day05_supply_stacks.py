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
    _source: int
    _destination: int

    @classmethod
    def from_text(cls, text) -> Instruction:
        match = re.match(r"move (\d+) from (\d+) to (\d+)", text)
        quantity, source, destination = match.groups()
        return cls(int(quantity), int(source), int(destination))

    @property
    def source(self) -> int:
        return self._source - 1

    @property
    def destination(self) -> int:
        return self._destination - 1


@dataclasses.dataclass
class Game:
    stacks: list[list[str]]
    instructions: list[Instruction]

    def play_instructions(self) -> None:
        for instruction in self.instructions:
            self.execute(instruction)

    def execute(self, instruction: Instruction) -> None:
        for _ in range(instruction.quantity):
            item = self.stacks[instruction.source].pop()
            self.stacks[instruction.destination].append(item)

    def message(self) -> str:
        msg = ""
        for stack in self.stacks:
            if stack:
                msg += stack[-1]
        return msg

    def __str__(self):
        return "\n".join(map(str, self.stacks))


DataType = Game


def parse_data(data: list[str]) -> DataType:
    stacks, instructions = data
    parsed_instructions = []
    for instruction in instructions.split("\n"):
        parsed_instructions.append(Instruction.from_text(instruction))
    stacks = list(stacks.split("\n")[::-1])
    header = stacks[0]
    parsed_stacks = []
    for index, char in enumerate(header):
        if char != " ":
            stack = []
            for row in stacks[1:]:
                char = row[index]
                if char == " ":
                    break
                stack.append(char)
            parsed_stacks.append(stack)
    return Game(parsed_stacks, parsed_instructions)


def solve_part_1(data: DataType) -> str:
    data.play_instructions()
    return data.message()


def solve_part_2(data: DataType) -> str:
    return "0"


if __name__ == "__main__":
    main("inputs/day05-test1", expected_part_1="CMZ")
    main("inputs/day05")
