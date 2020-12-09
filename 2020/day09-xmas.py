import copy
import itertools
from typing import List


def main(
    filename: str,
    expected_part_1: int = None,
    expected_part_2: int = None,
    preamble: int = 25,
):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        numbers = list(map(int, f.read().strip().split("\n")))  # type: List[int]

    pointer = preamble
    while pointer < len(numbers) and matches_rule(numbers, pointer, preamble):
        pointer += 1

    counter_part_1 = numbers[pointer]
    range_part_2 = sorted(find_range(numbers, counter_part_1))
    counter_part_2 = range_part_2[0] + range_part_2[-1]

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


def matches_rule(numbers, pointer, preamble):
    range_start = pointer - preamble
    range_end = pointer
    number = numbers[pointer]
    for combination in itertools.combinations(numbers[range_start:range_end], 2):
        if number == sum(combination):
            return True
    return False


def find_range(numbers, found_in_step_1):
    for i, start in enumerate(numbers):
        total = start
        j = i + 1
        while total < found_in_step_1 and j < len(numbers):
            total += numbers[j]
            j += 1
        if total == found_in_step_1:
            return numbers[i:j]
    raise Exception("Didn't find a valid range")


if __name__ == "__main__":
    main("inputs/day09-test1", 127, 62, preamble=5)
    main("inputs/day09", 144381670)
