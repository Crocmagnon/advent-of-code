from collections import defaultdict


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("\n")

    counter_part_1 = solve_part_1(data)

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    counter_part_2 = solve_part_2(data)
    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


def solve_part_1(data):
    count_ones = defaultdict(int)
    total = len(data)
    for binary in data:
        for index, digit in enumerate(binary):
            if digit == "1":
                count_ones[index] += 1
    gamma = ""
    epsilon = ""
    for index in range(len(data[0])):
        most_common = _most_common(count_ones, total, index)
        gamma += most_common
        epsilon += "0" if most_common == "1" else "1"
    return int(gamma, 2) * int(epsilon, 2)


def _most_common(count_ones, total, index):
    """
    Return 1 if the most common value is 1, otherwise 0.
    """
    if count_ones[index] >= total / 2:
        return "1"
    return "0"


def solve_part_2(data):
    oxygen = _oxygen(data)
    co2 = _co2(data)
    return oxygen * co2


def _oxygen(data):
    index = 0
    max_index = len(data[0])
    while index < max_index:
        if len(data) == 1:
            return int(data[0], 2)
        ones, zeros = _separate_ones_zeros(data, index)
        index += 1
        if len(ones) >= len(zeros):
            data = ones
        else:
            data = zeros
    return int(data[0], 2)


def _co2(data):
    index = 0
    max_index = len(data[0])
    while index < max_index:
        if len(data) == 1:
            return int(data[0], 2)
        ones, zeros = _separate_ones_zeros(data, index)
        index += 1
        if len(ones) < len(zeros):
            data = ones
        else:
            data = zeros


def _separate_ones_zeros(data, index):
    ones = []
    zeros = []
    for binary in data:
        if binary[index] == "1":
            ones.append(binary)
        else:
            zeros.append(binary)
    return ones, zeros


if __name__ == "__main__":
    main("inputs/day03-test1", expected_part_1=198, expected_part_2=230)
    main("inputs/day03", expected_part_1=1997414, expected_part_2=1032597)
