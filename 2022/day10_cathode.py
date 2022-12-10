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


DataType = list[str]


def parse_data(data: list[str]) -> DataType:
    return data


def solve_part_1(data: DataType) -> int:
    total = 0
    register = 1
    clock = 0
    expected_cycles = [20, 60, 100, 140, 180, 220]
    for instruction in data:
        match instruction.split():
            case ["noop"]:
                clock += 1
                if clock in expected_cycles:
                    print(f"{clock=}, {register=}")
                    total += register * clock
            case ["addx", value]:
                clock += 1
                if clock in expected_cycles:
                    print(f"{clock=}, {register=}")
                    total += register * clock
                clock += 1
                if clock in expected_cycles:
                    print(f"{clock=}, {register=}")
                    total += register * clock
                register += int(value)
    return total


def solve_part_2(data: DataType) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/day10-test1", expected_part_1=13140)
    main("inputs/day10")
