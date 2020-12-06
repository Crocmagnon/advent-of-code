from typing import List


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        groups = f.read().strip().split("\n\n")  # type: List[str]

    counter_part_1 = 0
    counter_part_2 = 0
    for group in groups:
        counter_part_1 += len(set(group.replace("\n", "")))
        people = group.split()
        intersect = set.intersection(*list(map(set, people)))
        counter_part_2 += len(intersect)

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


if __name__ == "__main__":
    main("inputs/day06-test1", 11, 6)
    main("inputs/day06-test2", 15, 8)
    main("inputs/day06", 6170, 2947)
