import enum
import functools
from typing import List


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        instructions = f.read().strip().split("\n")

    counter_part_1 = solve_part_1(instructions)

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    counter_part_2 = solve_part_2(instructions)
    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


def solve_part_1(instructions: List[str]):
    ship = ShipPart1()
    ship.apply_instructions(instructions)
    return ship.distance_from_origin


def solve_part_2(instructions: List[str]):
    ship = ShipPart2()
    ship.apply_instructions(instructions)
    return ship.distance_from_origin


class Ship:
    def __init__(self):
        self.vertical = 0
        self.horizontal = 0

    def apply_instructions(self, instructions):
        for instruction in instructions:
            self.apply_instruction(instruction)

    @property
    def distance_from_origin(self):
        return abs(self.vertical) + abs(self.horizontal)

    @staticmethod
    def parse_instruction(instruction):
        letter = instruction[0]
        value = int(instruction[1:])
        return letter, value

    def apply_instruction(self, instruction):
        raise NotImplementedError


class ShipPart1(Ship):
    def __init__(self):
        super().__init__()
        self.facing = Direction.EAST

    def apply_instruction(self, instruction):
        letter, value = self.parse_instruction(instruction)
        if letter in Direction.values():
            direction = Direction(letter)
            self.move(direction, value)
        elif letter == "F":
            self.move(self.facing, value)
        else:
            self.turn(letter, value)

    def move(self, direction: "Direction", value: int):
        if direction == Direction.NORTH:
            self.vertical += value
        elif direction == Direction.SOUTH:
            self.vertical -= value
        elif direction == Direction.EAST:
            self.horizontal += value
        else:
            self.horizontal -= value

    def turn(self, letter, value):
        if letter == "L":
            value = -value
        self.facing = self.facing.turn(value)


class ShipPart2(Ship):
    def __init__(self):
        super().__init__()
        self.waypoint = (10, 1)  # 10 units east, 1 unit north

    def apply_instruction(self, instruction):
        letter, value = self.parse_instruction(instruction)
        if letter in Direction.values():
            direction = Direction(letter)
            self.move_waypoint(direction, value)
        elif letter == "F":
            self.move_to_waypoint(value)
        else:
            if letter == "L":
                value = -value
            self.turn_waypoint(value)

    def move_waypoint(self, direction: "Direction", value: int):
        if direction in [Direction.NORTH, Direction.SOUTH]:
            if direction == Direction.SOUTH:
                value = -value
            self.waypoint = self.waypoint[0], self.waypoint[1] + value
        else:
            if direction == Direction.WEST:
                value = -value
            self.waypoint = self.waypoint[0] + value, self.waypoint[1]

    def move_to_waypoint(self, number_of_times: int):
        horizontal = self.waypoint[0] * number_of_times
        self.horizontal += horizontal
        vertical = self.waypoint[1] * number_of_times
        self.vertical += vertical

    def turn_waypoint(self, angle: int):
        if angle == 0:
            return
        horizontal = self.waypoint[0]
        vertical = self.waypoint[1]
        top_right_quadrant = vertical >= 0 and horizontal >= 0
        bottom_right_quadrant = vertical < 0 and horizontal >= 0
        bottom_left_quadrant = vertical < 0 and horizontal < 0
        if angle < 0:
            if top_right_quadrant:
                self.waypoint = -abs(vertical), abs(horizontal)
            elif bottom_right_quadrant:
                self.waypoint = abs(vertical), abs(horizontal)
            elif bottom_left_quadrant:
                self.waypoint = abs(vertical), -abs(horizontal)
            else:
                self.waypoint = -abs(vertical), -abs(horizontal)
            return self.turn_waypoint(angle + 90)
        else:
            if top_right_quadrant:
                self.waypoint = abs(vertical), -abs(horizontal)
            elif bottom_right_quadrant:
                self.waypoint = -abs(vertical), -abs(horizontal)
            elif bottom_left_quadrant:
                self.waypoint = -abs(vertical), abs(horizontal)
            else:
                self.waypoint = abs(vertical), abs(horizontal)
            return self.turn_waypoint(angle - 90)


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
    main("inputs/day12-test1", 25, 286)
    main("inputs/day12-test2", None, 202)
    main("inputs/day12", 1177, 46530)
