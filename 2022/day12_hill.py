from __future__ import annotations

import dataclasses
import math

import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path


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


@dataclasses.dataclass(frozen=True)
class Cell:
    x: int
    y: int
    value: int
    start: bool
    end: bool

    def can_move_to(self, other: Cell) -> bool:
        return other.value <= self.value + 1


@dataclasses.dataclass
class Hill:
    cells: list[Cell]
    start: Cell
    end: Cell
    width: int
    height: int
    potential_starters: list[Cell]
    graph: nx.DiGraph = None

    def top(self, cell: Cell) -> Cell | None:
        if cell.y == 0:
            return None
        index = self.index_from_coords(cell.x, cell.y - 1)
        return self.cells[index]

    def bottom(self, cell: Cell) -> Cell | None:
        if cell.y == self.height - 1:
            return None
        index = self.index_from_coords(cell.x, cell.y + 1)
        return self.cells[index]

    def left(self, cell: Cell) -> Cell | None:
        if cell.x == 0:
            return None
        index = self.index_from_coords(cell.x - 1, cell.y)
        return self.cells[index]

    def right(self, cell: Cell) -> Cell | None:
        if cell.x == self.width - 1:
            return None
        index = self.index_from_coords(cell.x + 1, cell.y)
        return self.cells[index]

    def index_from_coords(self, x: int, y: int) -> int:
        return y * self.width + x

    def build_graph(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(self.cells)
        for cell in self.cells:
            candidates = [
                self.top(cell),
                self.right(cell),
                self.bottom(cell),
                self.left(cell),
            ]
            for candidate in filter(None, candidates):
                if cell.can_move_to(candidate):
                    graph.add_edge(cell, candidate)
        self.graph = graph


DataType = Hill


def parse_data(data: list[str]) -> DataType:
    cells = []
    start_cell = None
    end_cell = None
    height = len(data)
    width = len(data[0])
    potential_starters = []
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            start, end = False, False
            if char == "S":
                start = True
                char = "a"
            elif char == "E":
                end = True
                char = "z"
            value = ord(char) - ord("a") + 1
            cell = Cell(x, y, value, start, end)
            if start:
                start_cell = cell
            elif end:
                end_cell = cell
            cells.append(cell)
            if char == "a":
                potential_starters.append(cell)
    hill = Hill(cells, start_cell, end_cell, width, height, potential_starters)
    hill.build_graph()
    return hill


def solve_part_1(data: DataType) -> int:
    path = shortest_path(data.graph, data.start, data.end)
    return len(path) - 1


def solve_part_2(data: DataType) -> int:
    min_length = math.inf
    for candidate in data.potential_starters:
        try:
            path = shortest_path(data.graph, candidate, data.end)
            path_length = len(path)
        except nx.NetworkXNoPath:
            path_length = math.inf
        if path_length < min_length:
            min_length = path_length
    return min_length - 1


if __name__ == "__main__":
    main("inputs/day12-test1", expected_part_1=31, expected_part_2=29)
    main("inputs/day12", expected_part_1=456, expected_part_2=454)
