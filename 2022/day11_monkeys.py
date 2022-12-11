from __future__ import annotations

import dataclasses


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("\n\n")

    data = parse_data(data)
    solution_part_1 = solve_part_1(data)

    print(f"1. Found {solution_part_1}")
    if expected_part_1:
        assert expected_part_1 == solution_part_1

    solution_part_2 = solve_part_2(data)
    print(f"2. Found {solution_part_2}")
    if expected_part_2:
        assert expected_part_2 == solution_part_2


@dataclasses.dataclass
class Operation:
    multiplier: int = 1
    adder: int = 0
    square: bool = False

    def compute(self, value: int) -> int:
        if self.square:
            value = value * value
        else:
            value = value * self.multiplier + self.adder

        return int(value / 3)


@dataclasses.dataclass
class Monkey:
    game: Game
    items: list[int]
    divisible_by: int
    true_monkey: int
    false_monkey: int
    operation: Operation
    inspected_items: int = 0

    @classmethod
    def from_input(cls, text: str, game: Game) -> Monkey:
        monkey_description = text.split("\n")
        items = []
        operation = None
        divisible_by = 1
        true_monkey = 0
        false_monkey = 0
        for line in monkey_description[1:]:
            match line.strip().split(": "):
                case ["Starting items", text_items]:
                    items = [int(item) for item in text_items.split(", ")]
                case ["Operation", text_operation]:
                    match text_operation.split():
                        case ["new", "=", "old", "*", "old"]:
                            operation = Operation(square=True)
                        case ["new", "=", "old", "*", multiplier]:
                            operation = Operation(multiplier=int(multiplier))
                        case ["new", "=", "old", "+", adder]:
                            operation = Operation(adder=int(adder))
                case ["Test", text_test]:
                    divisible_by = int(text_test.replace("divisible by", "").strip())
                case ["If true", text_target]:
                    true_monkey = int(
                        text_target.replace("throw to monkey", "").strip()
                    )
                case ["If false", text_target]:
                    false_monkey = int(
                        text_target.replace("throw to monkey", "").strip()
                    )
        monkey = Monkey(game, items, divisible_by, true_monkey, false_monkey, operation)
        game.monkeys.append(monkey)
        return monkey

    def play_round(self) -> None:
        self.inspected_items += len(self.items)
        for item in self.items:
            new_value = self.operation.compute(item)
            if new_value % self.divisible_by == 0:
                self.throw(self.true_monkey, new_value)
            else:
                self.throw(self.false_monkey, new_value)
        self.items = []

    def throw(self, target: int, item: int) -> None:
        self.game.monkeys[target].items.append(item)

    def print(self) -> None:
        print(", ".join(str(item) for item in self.items))


@dataclasses.dataclass
class Game:
    monkeys: list[Monkey] = dataclasses.field(default_factory=list)

    def play_round(self) -> None:
        for monkey in self.monkeys:
            monkey.play_round()

    def get_ranked_monkeys(self) -> list[Monkey]:
        return sorted(
            self.monkeys, key=lambda monkey: monkey.inspected_items, reverse=True
        )

    def print_monkeys(self) -> None:
        for index, monkey in enumerate(self.monkeys):
            print(f"Monkey {index}", end=": ")
            monkey.print()


DataType = Game


def parse_data(data: list[str]) -> DataType:
    game = Game()
    for text in data:
        Monkey.from_input(text, game)
    return game


def solve_part_1(game: DataType) -> int:
    for _ in range(1, 21):
        game.play_round()
    sorted_monkeys = game.get_ranked_monkeys()
    return sorted_monkeys[0].inspected_items * sorted_monkeys[1].inspected_items


def solve_part_2(data: DataType) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/day11-test1", expected_part_1=10605)
    main("inputs/day11", expected_part_1=95472)
