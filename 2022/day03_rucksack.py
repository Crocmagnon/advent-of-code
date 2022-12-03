import string


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("\n")

    data_1 = parse_data(data)
    solution_part_1 = solve_part_1(data_1)

    print(f"1. Found {solution_part_1}")
    if expected_part_1:
        assert expected_part_1 == solution_part_1

    solution_part_2 = solve_part_2(data)
    print(f"2. Found {solution_part_2}")
    if expected_part_2:
        assert expected_part_2 == solution_part_2


DataType = list[tuple[str, str]]


def parse_data(data: list[str]) -> DataType:
    sacks = []
    for line in data:
        stop = int(len(line) /2)
        halves = (line[:stop], line[stop:])
        sacks.append(halves)
    return sacks


def solve_part_1(data: DataType) -> int:
    total = 0
    for halves in data:
        first_half, second_half = set(halves[0]), set(halves[1])
        common_letter = first_half.intersection(second_half).pop()
        total += string.ascii_letters.index(common_letter) + 1
    return total


def solve_part_2(data: list[str]) -> int:
    total = 0
    for chunk in chunks(data, 3):
        common_letter = set(chunk[0]).intersection(set(chunk[1])).intersection(set(chunk[2])).pop()
        total += string.ascii_letters.index(common_letter) + 1
    return total


def chunks(data, size):
    for i in range(0, len(data), size):
        yield data[i:i+size]

if __name__ == "__main__":
    main("inputs/day03-test1", expected_part_1=157, expected_part_2=70)
    main("inputs/day03", expected_part_1=7716, expected_part_2=2973)
