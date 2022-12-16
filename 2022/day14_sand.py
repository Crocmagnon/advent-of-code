from __future__ import annotations


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        data = f.read().strip().split("\n")

    data, deepest_wall = parse_data(data)
    solution_part_1 = solve_part_1(data, deepest_wall)

    print(f"1. Found {solution_part_1}")
    if expected_part_1:
        assert expected_part_1 == solution_part_1

    solution_part_2 = solve_part_2(data)
    print(f"2. Found {solution_part_2}")
    if expected_part_2:
        assert expected_part_2 == solution_part_2


Point = tuple[int, int]
Walls = set(Point)


def generate_wall(start: Point, end: Point) -> Walls:
    walls = {start, end}
    if start == end:
        return {start}
    elif start[0] == end[0]:
        ys = (start[1], end[1])
        for y in range(min(ys) + 1, max(ys)):
            walls.add((start[0], y))
    elif start[1] == end[1]:
        xs = (start[0], end[0])
        for x in range(min(xs) + 1, max(xs)):
            walls.add((x, start[1]))
    return walls


def parse_data(data: list[str]) -> Walls:
    walls = set()
    deepest_wall = 0
    for line in data:
        angles = []
        for angle in line.split(" -> "):
            angles.append(tuple(map(int, angle.split(","))))
        for start, end in zip(angles[:-1], angles[1:]):
            if start[1] > deepest_wall:
                deepest_wall = start[1]
            if end[1] > deepest_wall:
                deepest_wall = end[1]
            walls.update(generate_wall(start, end))
    return walls, deepest_wall


def solve_part_1(walls: Walls, deepest_wall: int) -> int:
    sand_source = (500, 0)
    sand: Walls = set()
    while True:
        sand_x, sand_y = sand_source
        while sand_y < deepest_wall:
            if (sand_x, sand_y + 1) not in walls | sand:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in walls | sand:
                sand_x -= 1
                sand_y += 1
            elif (sand_x + 1, sand_y + 1) not in walls | sand:
                sand_x += 1
                sand_y += 1
            else:
                sand.add((sand_x, sand_y))
                break
        if sand_y >= deepest_wall:
            return len(sand)


def solve_part_2(walls: Walls) -> int:
    return 0


if __name__ == "__main__":
    main("inputs/day14-test1", expected_part_1=24)
    main("inputs/day14", expected_part_1=843)
