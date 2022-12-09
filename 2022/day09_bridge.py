from __future__ import annotations

import dataclasses


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


Instruction = tuple[str, int]
DataType = list[Instruction]


@dataclasses.dataclass
class Point:
    x: int = 0
    y: int = 0

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def move(self, instruction: Instruction) -> None:
        match instruction[0]:
            case "R":
                self.x += 1
            case "L":
                self.x -= 1
            case "U":
                self.y += 1
            case "D":
                self.y -= 1

    def follow(self, other: Point) -> None:
        if self == other:
            return
        if abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1:
            return
        if other.x > self.x:
            self.x += 1
        elif other.x < self.x:
            self.x -= 1
        if other.y > self.y:
            self.y += 1
        elif other.y < self.y:
            self.y -= 1

    @property
    def tuple(self) -> tuple[int, int]:
        return self.x, self.y


def parse_data(data: list[str]) -> DataType:
    instructions = []
    for line in data:
        direction, count = line.split()
        instructions.append((direction, int(count)))
    return instructions


def solve_part_1(instructions: DataType) -> int:
    head = Point()
    tail = Point()
    visited = set()
    for instruction in instructions:
        count = instruction[1]
        while count > 0:
            head.move(instruction)
            tail.follow(head)
            tail_tuple = tail.tuple
            visited.add(tail_tuple)
            count -= 1
    return len(visited)


def solve_part_2(instructions: DataType) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/day09-test1", expected_part_1=13)
    main("inputs/day09", expected_part_1=5619)
