import collections
import math


def already_seen_on_others(seen, wire, position):
    for key, value in seen.items():
        if key != wire and position in value:
            return value[position]
    return None


def distance(seen, position, wire_length):
    return int(math.fabs(position[0]) + math.fabs(position[1]))


def main():
    with open("inputs/day03") as f:
        raw = f.read()

    distances = set()
    seen_positions = collections.defaultdict(dict)
    for wire, line in enumerate(raw.split()):
        x, y = 0, 0
        wire_length = 0
        for segment in line.split(","):
            direction = segment[0]
            length = int(segment[1:])
            for _ in range(length):
                if direction == "R":
                    x += 1
                elif direction == "U":
                    y += 1
                elif direction == "L":
                    x -= 1
                elif direction == "D":
                    y -= 1
                else:
                    raise ValueError(f"Unknown direction: {direction}")
                wire_length += 1
                position = (x, y)
                if position not in seen_positions[wire]:
                    seen_positions[wire][position] = wire_length
                steps = already_seen_on_others(seen_positions, wire, position)
                if steps:
                    distances.add(steps + seen_positions[wire][position])

    print(min(distances))


if __name__ == "__main__":
    main()
