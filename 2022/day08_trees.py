import copy
from collections.abc import Iterable
from functools import partial


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("\n")

    data = parse_data(data)
    visible_trees = solve_part_1(data)
    solution_part_1 = len(visible_trees)

    print(f"1. Found {solution_part_1}")
    if expected_part_1:
        assert expected_part_1 == solution_part_1

    solution_part_2 = solve_part_2(data, visible_trees)
    print(f"2. Found {solution_part_2}")
    if expected_part_2:
        assert expected_part_2 == solution_part_2


Forest = DataType = list[list[int]]
Tree = tuple[int, int]


def parse_data(data: list[str]) -> DataType:
    grid = []
    for row in data:
        grid.append(list(map(int, row)))
    return grid


def solve_part_1(forest: DataType) -> set[Tree]:
    visible = set()
    forest = copy.deepcopy(forest)
    visible.update(find_visible_in_rows(forest))

    forest = map(list, zip(*forest))  # transpose grid so cols become rows
    visible.update(find_visible_in_rows(forest, swap=True))
    return visible


def find_visible_in_rows(forest: Iterable[list[int]], swap: bool = False) -> set[Tree]:
    visible = set()
    for row, trees in enumerate(forest):
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


def visible_tree(row: int, col: int, swap: bool) -> Tree:
    if swap:
        return col, row
    else:
        return row, col


def solve_part_2(forest: DataType, visible_trees: set[Tree]) -> int:
    # Hypothesis: the tree with the highest scenic score
    # is visible from the outside.
    max_scenic_score = 0
    for tree in filter(partial(is_inside, forest=forest), visible_trees):
        scenic_score = compute_scenic_score(tree, forest)
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
    return max_scenic_score


def is_border(tree: Tree, forest: DataType) -> bool:
    return 0 in tree or tree[0] == len(forest) - 1 or tree[1] == len(forest[0]) - 1


def is_inside(tree: Tree, forest: DataType) -> bool:
    return not is_border(tree, forest)


def compute_scenic_score(tree: Tree, forest: Forest) -> int:
    row, col = tree
    reference = forest[row][col]
    top = 0
    while row > 0:
        row -= 1
        top += 1
        visited = forest[row][col]
        if visited >= reference:
            break
    row, col = tree
    bottom = 0
    while row < len(forest) - 1:
        row += 1
        bottom += 1
        visited = forest[row][col]
        if visited >= reference:
            break
    row, col = tree
    left = 0
    while col > 0:
        col -= 1
        left += 1
        visited = forest[row][col]
        if visited >= reference:
            break
    row, col = tree
    right = 0
    while col < len(forest[0]) - 1:
        col += 1
        right += 1
        visited = forest[row][col]
        if visited >= reference:
            break
    return right * left * top * bottom


if __name__ == "__main__":
    main("inputs/day08-test1", expected_part_1=21, expected_part_2=8)
    main("inputs/day08", expected_part_1=1690)
