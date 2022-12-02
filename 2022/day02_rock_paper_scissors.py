from __future__ import annotations

import dataclasses
import enum

import pytest


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("\n")

    parsed_data = parse_data_part_1(data)
    solution_part_1 = solve_part_1(parsed_data)

    print(f"1. Found {solution_part_1}")
    if expected_part_1:
        assert expected_part_1 == solution_part_1

    parsed_data = parse_data_part_2(data)
    solution_part_2 = solve_part_2(parsed_data)
    print(f"2. Found {solution_part_2}")
    if expected_part_2:
        assert expected_part_2 == solution_part_2


class Shape(enum.IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def from_input(cls, letter: str) -> Shape:
        return {
            "A": cls.ROCK,
            "B": cls.PAPER,
            "C": cls.SCISSORS,
            "X": cls.ROCK,
            "Y": cls.PAPER,
            "Z": cls.SCISSORS,
        }[letter]

    def winner_for_opponent(self) -> Shape:
        return {
            self.SCISSORS: self.ROCK,
            self.ROCK: self.PAPER,
            self.PAPER: self.SCISSORS,
        }[self]

    def loser_for_opponent(self) -> Shape:
        return {
            self.ROCK: self.SCISSORS,
            self.PAPER: self.ROCK,
            self.SCISSORS: self.PAPER,
        }[self]


@dataclasses.dataclass
class Round:
    opponent: Shape
    me: Shape | None = None

    @property
    def value(self) -> int:
        return self.me.value + self.score

    @property
    def score(self) -> int:
        if self.victory:
            return 6
        elif self.draw:
            return 3
        else:
            return 0

    @property
    def victory(self) -> bool:
        return (self.me.value - self.opponent.value % 3) == 1

    @property
    def draw(self) -> bool:
        return self.opponent == self.me

    def complete(self, instruction: str):
        if instruction == "X":
            self.me = self.opponent.loser_for_opponent()
        elif instruction == "Y":
            self.me = self.opponent
        else:
            self.me = self.opponent.winner_for_opponent()


DataType = list[Round]


def parse_data_part_1(data: list[str]) -> DataType:
    rounds = []
    for round in data:  # noqa: A001
        opponent, me = round.split(" ")
        rounds.append(Round(Shape.from_input(opponent), Shape.from_input(me)))
    return rounds


def parse_data_part_2(data: list[str]) -> DataType:
    rounds = []
    for round in data:  # noqa: A001
        opponent, instruction = round.split(" ")
        r = Round(Shape.from_input(opponent))
        r.complete(instruction)
        rounds.append(r)
    return rounds


def solve_part_1(data: DataType) -> int:
    return sum([round.value for round in data])  # noqa: A001


def solve_part_2(data: DataType) -> int:
    return sum([round.value for round in data])  # noqa: A001


@pytest.mark.parametrize(
    "opponent,me",
    [
        (Shape.ROCK, Shape.PAPER),
        (Shape.PAPER, Shape.SCISSORS),
        (Shape.SCISSORS, Shape.ROCK),
    ],
)
def test_round_victory(opponent, me):
    round = Round(opponent, me)  # noqa: A001
    assert round.victory
    assert not round.draw


@pytest.mark.parametrize(
    "opponent,me",
    [
        (Shape.ROCK, Shape.ROCK),
        (Shape.PAPER, Shape.PAPER),
        (Shape.SCISSORS, Shape.SCISSORS),
    ],
)
def test_round_draw(opponent, me):
    round = Round(opponent, me)  # noqa: A001
    assert not round.victory
    assert round.draw


@pytest.mark.parametrize(
    "opponent,me",
    [
        (Shape.PAPER, Shape.ROCK),
        (Shape.SCISSORS, Shape.PAPER),
        (Shape.ROCK, Shape.SCISSORS),
    ],
)
def test_round_defeat(opponent, me):
    round = Round(opponent, me)  # noqa: A001
    assert not round.victory
    assert not round.draw


if __name__ == "__main__":
    main("inputs/day02-test1", expected_part_1=15, expected_part_2=12)
    main("inputs/day02", expected_part_1=12156, expected_part_2=10835)
