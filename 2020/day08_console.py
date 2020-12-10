import copy
from typing import List


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        program = f.read().strip().split("\n")  # type: List[str]

    counter_part_1, _ = run_until_infinite_loop_or_end(program)

    pointer = 0
    infinite = True
    while pointer < len(program) and infinite:
        program_copy = copy.deepcopy(program)
        instruction = program_copy[pointer]
        if "jmp" in instruction:
            program_copy[pointer] = instruction.replace("jmp", "nop")
        elif "nop" in instruction:
            program_copy[pointer] = instruction.replace("nop", "jmp")
        counter_part_2, infinite = run_until_infinite_loop_or_end(program_copy)
        pointer += 1

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


def run_until_infinite_loop_or_end(program):
    """
    Run the program until it ends or it loops infinitely.
    Returns the value of the accumulator before the end or the infinite loop
    and a boolean indicating whether the program terminated because of a loop (True)
    or a normal termination (False).
    """
    accumulator = 0
    visited = set()
    pointer = 0
    while pointer < len(program) and pointer not in visited:
        visited.add(pointer)
        instruction, argument = program[pointer].split()
        argument = int(argument)
        if instruction == "acc":
            accumulator += argument
            pointer += 1
        elif instruction == "jmp":
            pointer += argument
        else:
            pointer += 1
    return accumulator, pointer in visited


if __name__ == "__main__":
    main("inputs/day08-test1", 5, 8)
    main("inputs/day08", 1087, 780)
