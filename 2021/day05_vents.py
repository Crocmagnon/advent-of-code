from dataclasses import dataclass
from typing import List, Set


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


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class Segment:
    start: Point
    end: Point

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x

    def get_points(self) -> Set[Point]:
        if self.is_horizontal():
            start = min(self.start.x, self.end.x)
            end = max(self.start.x, self.end.x)
            return {Point(x, self.start.y) for x in range(start, end + 1)}
        elif self.is_vertical():
            start = min(self.start.y, self.end.y)
            end = max(self.start.y, self.end.y)
            return {Point(self.start.x, y) for y in range(start, end + 1)}
        return set()


def parse_data(data: List[str]) -> List[Segment]:
    segments = []
    for line in data:
        start, end = line.split(" -> ")
        start = start.split(",")
        end = end.split(",")
        start = Point(int(start[0]), int(start[1]))
        end = Point(int(end[0]), int(end[1]))
        segment = Segment(start, end)
        segments.append(segment)
    return segments


def solve_part_1(data: List[Segment]) -> int:
    seen_points = set()
    multiple_times = set()
    for segment in data:
        for point in segment.get_points():
            if point in seen_points:
                multiple_times.add(point)
            seen_points.add(point)
    return len(multiple_times)


def solve_part_2(data: List[Segment]) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/day05-test1", expected_part_1=5)
    main("inputs/day05", expected_part_1=7297)
