import itertools
from typing import List, Set, TypeAlias

Numbers: TypeAlias = List[int]
Grid: TypeAlias = List[Numbers]


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("\n\n")

    numbers, grids = parse_data(data)
    solution_part_1 = solve_part_1(numbers, grids)

    print(f"1. Found {solution_part_1}")
    if expected_part_1:
        assert expected_part_1 == solution_part_1

    solution_part_2 = solve_part_2(numbers, grids)
    print(f"2. Found {solution_part_2}")
    if expected_part_2:
        assert expected_part_2 == solution_part_2


def parse_data(data: List[str]) -> (Numbers, List[Grid]):
    numbers: Numbers = list(map(int, data[0].split(",")))
    data = data[1:]
    grids: List[Grid] = []
    for grid in data:
        parsed_grid: Grid = []
        grid_lines = grid.split("\n")
        for line in grid_lines:
            line = list(map(int, line.split()))
            parsed_grid.append(line)
        grids.append(parsed_grid)
    return numbers, grids


def solve_part_1(numbers: Numbers, grids: List[Grid]) -> int:
    seen: Set[int] = set()
    for number in numbers:
        seen.add(number)
        for grid in grids:
            if check_bingo(grid, seen):
                return sum(unseen(grid, seen)) * number


def check_bingo(grid: Grid, seen: Set[int]) -> bool:
    return check_row(grid, seen) or check_column(grid, seen)


def check_row(grid: Grid, seen: Set[int]) -> bool:
    for row in grid:
        if check_line(row, seen):
            return True
    return False


def check_column(grid: Grid, seen: Set[int]) -> bool:
    for i in range(len(grid[0])):
        column = [row[i] for row in grid]
        if check_line(column, seen):
            return True
    return False


def check_line(line: Numbers, seen: Set[int]) -> bool:
    for number in line:
        if number not in seen:
            return False
    return True


def unseen(grid: Grid, seen: Set[int]) -> Numbers:
    return [n for n in itertools.chain.from_iterable(grid) if n not in seen]


def solve_part_2(numbers: Numbers, grids: List[Grid]) -> int:
    seen: Set[int] = set()
    score = 0
    winners: Set[int] = set()
    for number in numbers:
        seen.add(number)
        for index, grid in enumerate(grids):
            if index in winners:
                continue
            if check_bingo(grid, seen):
                score = sum(unseen(grid, seen)) * number
                winners.add(index)
    return score


if __name__ == "__main__":
    main("inputs/day04-test1", expected_part_1=4512, expected_part_2=1924)
    main("inputs/day04", expected_part_1=23177)
