from __future__ import annotations

import dataclasses
import math


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("$ ")

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
class File:
    name: str
    size: int

    def __str__(self):
        return f"- {self.name} (file, size={self.size})"

    def print(self, level: int = 0):
        print(" " * level * 2 + str(self))

    @property
    def is_directory(self) -> bool:
        return False


@dataclasses.dataclass
class Directory:
    name: str
    parent: Directory = None
    children: list[File | Directory] = dataclasses.field(default_factory=list)

    def __str__(self):
        return f"- {self.name} (dir, size={self.size})"

    def print(self, level: int = 0):
        print(" " * level * 2 + str(self))
        for child in self.children:
            child.print(level + 1)

    def root(self):
        if self.parent:
            return self.parent.root()
        else:
            return self

    @property
    def size(self) -> int:
        return sum(child.size for child in self.children)

    @property
    def is_directory(self) -> bool:
        return True


def parse_data(commands: list[str]) -> Directory:
    current_directory = None
    for command in commands:
        command, *result = command.strip().split("\n")
        match command.split():
            case ["cd", ".."]:
                current_directory = current_directory.parent
            case ["cd", dir_name]:
                new_dir = Directory(dir_name, parent=current_directory)
                if current_directory:
                    current_directory.children.append(new_dir)
                current_directory = new_dir
            case ["ls"]:
                for line in result:
                    match line.split():
                        case ["dir", _]:
                            pass
                        case [size, name]:
                            current_directory.children.append(File(name, int(size)))

    return current_directory.root()


def solve_part_1(root: Directory) -> int:
    total = 0
    to_visit = [root]
    while to_visit:
        visited = to_visit.pop()
        to_visit.extend([child for child in visited.children if child.is_directory])
        size = visited.size
        if size <= 100000:
            total += size
    return total


def solve_part_2(root: Directory) -> int:
    total_disk_space = 70000000
    required_disk_space = 30000000
    unused_space = total_disk_space - root.size
    minimum_size_to_delete = required_disk_space - unused_space
    minimum_directory_size = math.inf
    to_visit = [root]
    while to_visit:
        visited = to_visit.pop()
        to_visit.extend([child for child in visited.children if child.is_directory])
        size = visited.size
        if minimum_size_to_delete <= size <= minimum_directory_size:
            minimum_directory_size = size
    return minimum_directory_size


if __name__ == "__main__":
    main("inputs/day07-test1", expected_part_1=95437)
    main("inputs/day07", expected_part_1=1517599)
