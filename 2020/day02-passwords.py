from collections import Counter
from typing import Tuple


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    counter_part_1 = 0
    counter_part_2 = 0
    with open(filename) as f:
        for line in f:
            if is_valid_part_1(*extract_password_and_policy(line)):
                counter_part_1 += 1
            if is_valid_part_2(*extract_password_and_policy(line)):
                counter_part_2 += 1

    print(f"Part1: Found {counter_part_1} valid passwords.")
    print(f"Part2: Found {counter_part_2} valid passwords.")
    if expected_part_1:
        assert counter_part_1 == expected_part_1
    if expected_part_2:
        assert counter_part_2 == expected_part_2


def extract_password_and_policy(line) -> Tuple[Tuple[int, int], str, str]:
    policy, password = line.strip().split(": ")
    rng, letter = policy.split(" ")
    rng = tuple(map(int, rng.split("-")))
    return rng, letter, password


def is_valid_part_1(rng: Tuple[int, int], letter: str, password: str):
    counter = Counter(password)
    return rng[0] <= counter[letter] <= rng[1]


def is_valid_part_2(rng: Tuple[int, int], letter: str, password: str):
    first_index = password[rng[0]-1]
    second_index = password[rng[1]-1]
    return first_index != second_index and (first_index == letter or second_index == letter)


if __name__ == '__main__':
    main("inputs/day02-tests", 2, 1)
    main("inputs/day02")
