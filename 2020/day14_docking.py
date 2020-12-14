import functools
import re
from typing import List, Dict, Iterable, Union


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

    program = ProgramPart2(instructions)
    program.run()
    counter_part_2 = program.compute_memory_sum()
    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


Memory = Dict[Union[str, int], Union[str, int]]


class Program:
    def __init__(self, instructions: Iterable[str]):
        self.memory = dict()  # type: Memory
        self.instructions = instructions
        self.mem_line_regex = re.compile(r"^mem\[(?P<address>\d+)] = (?P<value>\d+)$")

    def run(self):
        for line in self.instructions:
            self.run_line(line)

    def compute_memory_sum(self):
        raise NotImplementedError

    def run_line(self, line: str):
        if "mask" in line:
            self.update_mask(line)
        else:
            self.update_memory(line)

    def update_mask(self, line: str):
        self.mask = line.split(" = ")[1]

    def update_memory(self, line: str):
        raise NotImplementedError


class ProgramPart1(Program):
    def __init__(self, instructions: Iterable[str]):
        super().__init__(instructions)
        self.mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    def compute_memory_sum(self):
        int_base_2 = functools.partial(int, base=2)
        return sum(map(int_base_2, self.memory.values()))

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


class ProgramPart2(Program):
    def __init__(self, instructions: Iterable[str]):
        super().__init__(instructions)
        self.mask = "000000000000000000000000000000000000"

    def compute_memory_sum(self):
        return sum(self.memory.values())

    def update_memory(self, line: str):
        match = self.mem_line_regex.match(line)
        if not match:
            raise RuntimeError("Memory line regex doesn't match")
        groups = match.groupdict()
        address = int(groups["address"])
        value = int(groups["value"])
        for masked_address in self.get_masked_addresses(address):
            self.memory[masked_address] = value

    def get_masked_addresses(self, address: int) -> Iterable[int]:
        binary_address = "{:036b}".format(address)
        corrected_binary_address = ""
        for binary_bit, mask_bit in zip(binary_address, self.mask):
            if mask_bit == "1":
                corrected_binary_address += "1"
            else:
                corrected_binary_address += binary_bit
        addresses = self.get_floating_addresses("", corrected_binary_address, self.mask)
        int_base_2 = functools.partial(int, base=2)
        return map(int_base_2, addresses)

    def get_floating_addresses(self, prefix: str, address: str, mask: str) -> List[str]:
        if "X" not in mask:
            return [prefix + address]
        first_x = mask.index("X")
        collector = []
        new_address = address[first_x + 1 :]
        new_prefix = prefix + address[:first_x]
        new_mask = mask[first_x + 1 :]
        collector.extend(
            self.get_floating_addresses(new_prefix + "0", new_address, new_mask)
        )
        collector.extend(
            self.get_floating_addresses(new_prefix + "1", new_address, new_mask)
        )
        return collector


if __name__ == "__main__":
    # main("inputs/day14-test1", 165)  # too slow for part 2
    main("inputs/day14-test2", 51, 208)
    main("inputs/day14", 6559449933360, 3369767240513)
