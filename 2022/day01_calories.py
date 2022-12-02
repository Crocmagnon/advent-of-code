def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("\n\n")

    data = parse_data(data)
    solution_part_1 = solve_part_1(data)

    print(f"1. Found {solution_part_1}")
    if expected_part_1:
        assert expected_part_1 == solution_part_1

    solution_part_2 = solve_part_2(data)
    print(f"2. Found {solution_part_2}")
    if expected_part_2:
        assert expected_part_2 == solution_part_2


def parse_data(data: list[str]) -> list[int]:
    split_lines = []
    for group in data:
        split_lines.append(list(map(int, group.split("\n"))))
    sums = [sum(group) for group in split_lines]
    return sums


def solve_part_1(data: list[int]) -> int:
    return max(data)


def solve_part_2(data: list[int]) -> int:
    return sum(sorted(data, reverse=True)[:3])


if __name__ == "__main__":
    main("inputs/day01-test1", expected_part_1=24000, expected_part_2=45000)
    main("inputs/day01", expected_part_1=70296)
