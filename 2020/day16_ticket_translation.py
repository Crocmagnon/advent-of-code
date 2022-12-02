import re
from collections import defaultdict
from collections.abc import Iterable


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        blocks = f.read().strip().split("\n\n")

    analyser = TicketAnalyserPart1(blocks)
    counter_part_1 = analyser.get_error_rate()

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    columns_assignation = analyser.compute_class_assignation()
    counter_part_2 = analyser.get_departure_value(columns_assignation)
    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


Range = tuple[int, int]
Ranges = list[Range]


class TicketAnalyserPart1:
    def __init__(self, blocks):
        named_ranges = blocks[0].split("\n")
        self.ranges = {}
        for named_range in named_ranges:
            name, ranges = self.extract_ranges(named_range)
            self.ranges[name] = ranges
        self.my_ticket = list(map(int, blocks[1].split("\n")[1].split(",")))
        self.nearby_tickets = [
            list(map(int, ticket.split(","))) for ticket in blocks[2].split("\n")[1:]
        ]
        self.valid_tickets = []

    @staticmethod
    def extract_ranges(named_range: str) -> tuple[str, Ranges]:
        name, ranges = named_range.split(": ")
        reg = re.compile(r"(\d+)-(\d+) or (\d+)-(\d+)$")
        matches = reg.match(ranges)
        groups = [int(group) for group in matches.groups()]
        return name, [(groups[0], groups[1]), (groups[2], groups[3])]

    def get_error_rate(self) -> int:
        error_rate = 0
        for ticket in self.nearby_tickets:
            invalid_values = self.get_invalid_values(ticket)
            if invalid_values:
                error_rate += sum(invalid_values)
            else:
                self.valid_tickets.append(ticket)
        return error_rate

    def get_invalid_values(self, ticket: list[int]) -> list[int]:
        invalid_values = []
        for value in ticket:
            if self.value_is_invalid(value):
                invalid_values.append(value)
        return invalid_values

    def value_is_invalid(self, value: int, ranges: Iterable[Range] = None) -> bool:
        return not self.value_is_valid(value, ranges)

    def value_is_valid(self, value: int, ranges: Iterable[Range] = None) -> bool:
        if ranges is None:
            ranges = self.iter_ranges()
        for rng in ranges:
            if value in range(rng[0], rng[1] + 1):
                return True
        return False

    def iter_ranges(self) -> Iterable[Range]:
        for ranges in self.ranges.values():
            yield from ranges

    def compute_class_assignation(self):
        possible_columns_for_range = defaultdict(list)
        for name, ranges in self.ranges.items():
            for column in range(0, len(self.ranges)):
                if self.column_is_possible(ranges, column):
                    possible_columns_for_range[name].append(column)
        columns_assignation = {}
        sorted_keys = self.get_sorted_keys(possible_columns_for_range)
        for key in sorted_keys:
            assigned_column = possible_columns_for_range[key][0]
            columns_assignation[key] = assigned_column
            possible_columns_for_range = self.delete_assigned_column(
                possible_columns_for_range, assigned_column
            )
        return columns_assignation

    def get_departure_value(self, columns_assignation):
        total = 1
        for name, column in columns_assignation.items():
            if name.startswith("departure"):
                total *= self.my_ticket[column]
        return total

    def column_is_possible(self, ranges, column):
        for ticket in self.valid_tickets:
            if self.value_is_invalid(ticket[column], ranges):
                return False
        return True

    @staticmethod
    def get_sorted_keys(possible_columns_for_range):
        return [
            item[0]
            for item in sorted(
                [
                    (name, len(columns))
                    for name, columns in possible_columns_for_range.items()
                ],
                key=lambda x: x[1],
            )
        ]

    def delete_assigned_column(self, possible_columns_for_range, assigned_column):
        new_possible_columns = {}
        for name, columns in possible_columns_for_range.items():
            new_possible_columns[name] = [
                col for col in columns if col != assigned_column
            ]
        return new_possible_columns


if __name__ == "__main__":
    main("inputs/day16-test1", 71)
    main("inputs/day16", 32835, 514662805187)
