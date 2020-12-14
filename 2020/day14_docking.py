import enum
import functools
import math
import re
from typing import List, Dict, Iterable


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        instructions = f.read().strip().split("\n")

    program = ProgramPart1(instructions)
    program.run()
    counter_part_1 = program.compute_memory_sum()

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    counter_part_2 = solve_part_2(instructions)
    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


Memory = Dict[str, str]


class ProgramPart1:
    def __init__(self, instructions: Iterable[str]):
        self.memory = dict()  # type: Memory
        self.instructions = instructions
        self.mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        self.mem_line_regex = re.compile(r"^mem\[(?P<address>\d+)] = (?P<value>\d+)$")

    def run(self):
        for line in self.instructions:
            self.run_line(line)

    def compute_memory_sum(self):
        int_base_2 = functools.partial(int, base=2)
        return sum(map(int_base_2, self.memory.values()))

    def run_line(self, line: str):
        if "mask" in line:
            self.update_mask(line)
        else:
            self.update_memory(line)

    def update_mask(self, line: str):
        self.mask = line.split(" = ")[1]

    def update_memory(self, line: str):
        match = self.mem_line_regex.match(line)
        if not match:
            raise RuntimeError("Memory line regex doesn't match")
        groups = match.groupdict()
        address = groups["address"]
        value = int(groups["value"])
        self.memory[address] = self.get_masked_value(value)

    def get_masked_value(self, value: int) -> str:
        binary_value = "{:036b}".format(value)
        masked_value = []
        for binary_bit, mask_bit in zip(binary_value, self.mask):
            if mask_bit == "X":
                masked_value.append(binary_bit)
            else:
                masked_value.append(mask_bit)

        return "".join(masked_value)


def solve_part_2(program: Iterable[str]) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/day14-test1", 165)
    main("inputs/day14")
