import enum
import functools
from typing import List


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        instructions = f.read().strip().split("\n")

    counter_part_1 = solve_part_1(instructions)
    counter_part_2 = 0

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


def solve_part_1(instructions: List[str]):
    ship = Ship()
    ship.apply_instructions(instructions)
    return ship.distance_from_origin


class Ship:
    def __init__(self):
        self.facing = Direction.EAST
        self.movements = {
            Direction.NORTH: 0,
            Direction.SOUTH: 0,
            Direction.EAST: 0,
            Direction.WEST: 0,
        }

    def apply_instructions(self, instructions):
        for instruction in instructions:
            self.apply_instruction(instruction)

    @property
    def distance_from_origin(self):
        return abs(
            self.movements[Direction.NORTH] - self.movements[Direction.SOUTH]
        ) + abs(self.movements[Direction.EAST] - self.movements[Direction.WEST])

    def apply_instruction(self, instruction):
        letter = instruction[0]
        value = int(instruction[1:])
        if letter in Direction.values():
            direction = Direction(letter)
            self.move(direction, value)
        elif letter == "F":
            self.move(self.facing, value)
        elif letter in ["R", "L"]:
            if letter == "L":
                value = -value
            self.facing = self.facing.turn(value)

    def move(self, direction: "Direction", value: int):
        self.movements[direction] += value


class Direction(enum.Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"

    @staticmethod
    @functools.lru_cache(maxsize=1)
    def values():
        return {e.value for e in Direction}

    def turn(self, angle):
        if angle == 0:
            return self
        if self == Direction.NORTH:
            if angle > 0:
                return Direction.EAST.turn(angle - 90)
            else:
                return Direction.WEST.turn(angle + 90)
        if self == Direction.SOUTH:
            if angle > 0:
                return Direction.WEST.turn(angle - 90)
            else:
                return Direction.EAST.turn(angle + 90)
        if self == Direction.EAST:
            if angle > 0:
                return Direction.SOUTH.turn(angle - 90)
            else:
                return Direction.NORTH.turn(angle + 90)
        if self == Direction.WEST:
            if angle > 0:
                return Direction.NORTH.turn(angle - 90)
            else:
                return Direction.SOUTH.turn(angle + 90)


if __name__ == "__main__":
    main("inputs/day12-test1", 25)
    main("inputs/day12")
