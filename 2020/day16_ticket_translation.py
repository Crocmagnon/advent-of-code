import re
from functools import lru_cache
from typing import List, Tuple


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        blocks = f.read().strip().split("\n\n")

    counter_part_1 = solve_part_1(blocks)

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    counter_part_2 = solve_part_2(blocks)
    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


Range = Tuple[int, int]
Ranges = List[Range]


def solve_part_1(blocks):
    analyser = TicketAnalyserPart1(blocks)
    return analyser.get_error_rate()


class TicketAnalyserPart1:
    def __init__(self, blocks):
        named_ranges = blocks[0].split("\n")
        ranges = []
        for named_range in named_ranges:
            ranges.extend(self.extract_ranges(named_range))
        self.ranges = self.merge_ranges(ranges)
        self.nearby_tickets = blocks[2].split("\n")[1:]

    @staticmethod
    def extract_ranges(named_range: str) -> Ranges:
        reg = re.compile(r"^.*: (\d+)-(\d+) or (\d+)-(\d+)$")
        matches = reg.match(named_range)
        groups = [int(group) for group in matches.groups()]
        return [(groups[0], groups[1]), (groups[2], groups[3])]

    @staticmethod
    def merge_ranges(times) -> Ranges:
        ranges = []
        saved = list(times[0])
        for st, en in sorted([sorted(t) for t in times]):
            if st <= saved[1]:
                saved[1] = max(saved[1], en)
            else:
                ranges.append(tuple(saved))
                saved[0] = st
                saved[1] = en
        ranges.append(tuple(saved))
        return ranges

    def get_error_rate(self):
        error_rate = 0
        for ticket in self.nearby_tickets:
            error_rate += sum(self.get_invalid_values(ticket))
        return error_rate

    def get_invalid_values(self, ticket: str) -> List[int]:
        ticket = map(int, ticket.split(","))
        invalid_values = []
        for value in ticket:
            if self.value_is_invalid(value):
                invalid_values.append(value)
        return invalid_values

    @lru_cache(None)
    def value_is_invalid(self, value: int) -> bool:
        return not self.value_is_valid(value)

    def value_is_valid(self, value: int) -> bool:
        for rng in self.ranges:
            if value in range(rng[0], rng[1] + 1):
                return True
        return False


def solve_part_2(blocks):
    return 0


if __name__ == "__main__":
    main("inputs/day16-test1", 71)
    main("inputs/day16", 32835)
