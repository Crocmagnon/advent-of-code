from itertools import combinations
from math import prod


def main():
    lines = []
    with open("inputs/day01") as f:
        for line in f:
            lines.append(int(line.strip()))

    res = solve(lines, 2)
    print("result is", res)
    res = solve(lines, 3)
    print("result is", res)


def solve(expense_report, fix_number):
    for combination in combinations(expense_report, fix_number):
        if sum(combination) == 2020:
            return prod(combination)


if __name__ == "__main__":
    main()
