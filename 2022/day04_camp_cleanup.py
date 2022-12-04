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


DataType = tuple[set[int], set[int]]


def parse_data(data: list[str]) -> DataType:
    lines = []
    for line in data:
        first, second = line.split(",")
        first_1, first_2 = first.split("-")
        first = set(range(int(first_1), int(first_2)+1))
        second_1, second_2 = second.split("-")
        second = set(range(int(second_1), int(second_2)+1))
        lines.append((first, second))
    return lines


def solve_part_1(data: DataType) -> int:
    total = 0
    for line in data:
        first, second = line
        if first.issuperset(second) or second.issuperset(first):
            total += 1
    return total


def solve_part_2(data: DataType) -> int:
    total = 0
    for line in data:
        first, second = line
        if first.intersection(second) != set():
            total += 1
    return total


if __name__ == "__main__":
    main("inputs/day04-test1", expected_part_1=2, expected_part_2=4)
    main("inputs/day04", expected_part_1=413)
