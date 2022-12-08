import copy
from collections.abc import Iterable


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


DataType = list[list[int]]


def parse_data(data: list[str]) -> DataType:
    grid = []
    for row in data:
        grid.append(list(map(int, row)))
    return grid


def solve_part_1(grid: DataType) -> int:
    visible = set()
    grid = copy.deepcopy(grid)
    visible.update(find_visible_in_rows(grid))

    grid = map(list, zip(*grid))  # transpose grid so cols become rows
    visible.update(find_visible_in_rows(grid, swap=True))
    return len(visible)


def find_visible_in_rows(
    grid: Iterable[list[int]], swap: bool = False
) -> set[tuple[int, int]]:
    visible = set()
    for row, trees in enumerate(grid):
        max_height = -1
        for col, tree in enumerate(trees):
            if tree > max_height:
                max_height = tree
                visible.add(visible_tree(row, col, swap))
        max_height = -1
        for col, tree in enumerate(reversed(trees)):
            col = len(trees) - col - 1
            if tree > max_height:
                max_height = tree
                visible.add(visible_tree(row, col, swap))
    return visible


def visible_tree(row, col, swap):
    if swap:
        return col, row
    else:
        return row, col


def solve_part_2(data: DataType) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/day08-test1", expected_part_1=21)
    main("inputs/day08", expected_part_1=1690)
