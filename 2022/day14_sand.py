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

    solution_part_2 = solve_part_2(data, deepest_wall)
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
    sand: Walls = set()
    while True:
        sand_x, sand_y = compute_final_position(walls, sand, deepest_wall)
        if sand_y >= deepest_wall:
            print_grid(493, 503, 10, walls, sand)
            return len(sand)
        sand.add((sand_x, sand_y))


def compute_final_position(
    walls: Walls, sand: Walls, deepest_wall: int, floor_level: int | None = None
) -> Point:
    sand_x, sand_y = 500, 0
    while sand_y < deepest_wall:
        floor: Walls = set()
        if floor_level:
            floor = {
                (sand_x - 1, floor_level),
                (sand_x, floor_level),
                (sand_x + 1, floor_level),
            }
        if (sand_x, sand_y + 1) not in walls | sand | floor:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in walls | sand | floor:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in walls | sand | floor:
            sand_x += 1
            sand_y += 1
        else:
            return sand_x, sand_y
    return sand_x, sand_y


def print_grid(
    min_x: int,
    max_x: int,
    max_y: int,
    walls: Walls,
    sand: Walls,
    floor_level: int | None = None,
) -> None:
    for y in range(0, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) == (500, 0):
                print("+", end="")
            elif y == floor_level:
                print("#", end="")
            elif (x, y) in walls:
                print("#", end="")
            elif (x, y) in sand:
                print("o", end="")
            else:
                print(".", end="")
        print()


def solve_part_2(walls: Walls, deepest_wall: int) -> int:
    sand: Walls = set()
    sand_x, sand_y = 0, 0
    while (sand_x, sand_y) != (500, 0):
        sand_x, sand_y = compute_final_position(
            walls, sand, deepest_wall + 2, deepest_wall + 2
        )
        sand.add((sand_x, sand_y))
    return len(sand)


if __name__ == "__main__":
    main("inputs/day14-test1", expected_part_1=24, expected_part_2=93)
    main("inputs/day14", expected_part_1=843)
