from dataclasses import dataclass


@dataclass
class Asteroid:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def square_length(a: "Asteroid", b: "Asteroid"):
        return (b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y)

    @staticmethod
    def cross_product(a: "Asteroid", b: "Asteroid", c: "Asteroid"):
        return (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)

    @staticmethod
    def dot_product(a: "Asteroid", b: "Asteroid", c: "Asteroid"):
        return (c.x - a.x) * (b.x - a.x) + (c.y - a.y) * (b.y - a.y)

    @staticmethod
    def is_between(a: "Asteroid", b: "Asteroid", c: "Asteroid"):
        """Check if c is between a and b."""
        cross_product = Asteroid.cross_product(a, b, c)

        # compare versus epsilon for floating point values, or != 0 if using integers
        if abs(cross_product) != 0:
            return False

        dot_product = Asteroid.dot_product(a, b, c)
        if dot_product < 0:
            return False

        squared_length_ba = Asteroid.square_length(a, b)
        if dot_product > squared_length_ba:
            return False

        return True

    def can_see(self, other: "Asteroid", asteroids: set["Asteroid"]) -> bool:
        for asteroid in asteroids:
            if asteroid in [self, other]:
                continue
            if Asteroid.is_between(self, other, asteroid):
                return False
        return True


def main():
    asteroids = set()
    with open("inputs/day10") as f:
        for y, line in enumerate(f):
            for x, pixel in enumerate(line):
                if pixel == "#":
                    asteroids.add(Asteroid(x, y))

    max_visible = 0
    for source in asteroids:
        visible = 0
        for destination in asteroids:
            if destination != source and source.can_see(destination, asteroids):
                visible += 1
        if visible > max_visible:
            max_visible = visible
    print(max_visible)


if __name__ == "__main__":
    main()
