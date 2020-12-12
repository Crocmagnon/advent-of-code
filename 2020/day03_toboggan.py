from math import prod
from typing import List

TREE = "#"


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        forest = f.read().strip().split("\n")  # type: List[str]

    trees_31 = trees_for_slope(forest, right=3, down=1)
    print(f"Found {trees_31} trees for part 1")
    if expected_part_1:
        assert trees_31 == expected_part_1

    trees = [
        trees_31,
        trees_for_slope(forest, right=1, down=1),
        trees_for_slope(forest, right=5, down=1),
        trees_for_slope(forest, right=7, down=1),
        trees_for_slope(forest, right=1, down=2),
    ]
    print(f"Found these trees for part 2: {trees}")
    prod_trees = prod(trees)
    print(f"Found {prod_trees} trees for part 2")
    if expected_part_2:
        assert prod_trees == expected_part_2


def trees_for_slope(forest: List[str], right: int, down: int) -> int:
    trees = 0
    current_line = 0
    current_col = 0
    while current_line < len(forest):
        item = forest[current_line][current_col]
        if item == TREE:
            trees += 1
        current_col = (current_col + right) % len(forest[0])
        current_line += down
    return trees


if __name__ == "__main__":
    main("inputs/day03-tests", 7, 336)
    main("inputs/day03", 240, 2832009600)
