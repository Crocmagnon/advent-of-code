from dataclasses import dataclass


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

    def get_points_part_1(self) -> set[Point]:
        if self.is_horizontal():
            start = min(self.start.x, self.end.x)
            end = max(self.start.x, self.end.x)
            return {Point(x, self.start.y) for x in range(start, end + 1)}
        if self.is_vertical():
            start = min(self.start.y, self.end.y)
            end = max(self.start.y, self.end.y)
            return {Point(self.start.x, y) for y in range(start, end + 1)}
        return set()

    def get_points_part_2(self) -> set[Point]:
        part_1 = self.get_points_part_1()
        if part_1:
            return part_1

        x = self.start.x
        y = self.start.y
        point = Point(x, y)
        points = {point}
        while point != self.end:
            if x < self.end.x:
                x += 1
            else:
                x -= 1
            if y < self.end.y:
                y += 1
            else:
                y -= 1
            point = Point(x, y)
            points.add(point)
        return points


def parse_data(data: list[str]) -> list[Segment]:
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


def solve_part_1(data: list[Segment]) -> int:
    seen_points = set()
    multiple_times = set()
    for segment in data:
        for point in segment.get_points_part_1():
            if point in seen_points:
                multiple_times.add(point)
            seen_points.add(point)
    return len(multiple_times)


def solve_part_2(data: list[Segment]) -> int:
    seen_points = set()
    multiple_times = set()
    for segment in data:
        for point in segment.get_points_part_2():
            if point in seen_points:
                multiple_times.add(point)
            seen_points.add(point)
    return len(multiple_times)


if __name__ == "__main__":
    main("inputs/day05-test2", expected_part_1=2, expected_part_2=3)
    main("inputs/day05-test1", expected_part_1=5, expected_part_2=12)
    main("inputs/day05", expected_part_1=7297, expected_part_2=21038)
