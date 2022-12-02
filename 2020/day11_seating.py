import functools
from collections import Counter
from typing import Dict


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        seat_map = f.read()

    seat_map_part_1 = SeatMap(seat_map)
    seat_map_part_1.evolve_until_stable()
    counter_part_1 = seat_map_part_1.total_number_of_occupied()

    seat_map_part_2 = SeatMapPart2(seat_map)
    seat_map_part_2.evolve_until_stable()
    counter_part_2 = seat_map_part_2.total_number_of_occupied()

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


Coordinates = tuple[int, int]


class SeatMap:
    OCCUPIED = "#"
    FREE = "L"
    FLOOR = "."
    EMPTY_THRESHOLD = 4

    def __init__(self, seat_map: str):
        self._map = dict()  # type: Dict[Coordinates, str]
        rows = seat_map.split("\n")
        for row_id, row in enumerate(rows):
            for col_id, cell in enumerate(row):
                self._map[(row_id, col_id)] = cell
        self._map_height = len(rows)
        self._map_width = len(rows[0])

    def __str__(self):
        final = []
        for row_id in range(0, self._map_height):
            row = []
            for col_id in range(0, self._map_width):
                row.append(self._square_at((row_id, col_id)))
            final.append("".join(row))
        return "\n".join(final) + "\n"

    def _square_at(self, coordinates: Coordinates) -> str:
        return self._map[coordinates]

    def total_number_of_occupied(self) -> int:
        counter = Counter("".join(self._map.values()))
        return counter[self.OCCUPIED]

    def evolve_until_stable(self):
        old_map = self._map
        next_stage_map = self._evolve()
        while next_stage_map != old_map:
            old_map = next_stage_map
            next_stage_map = self._evolve()

    def _evolve(self):
        next_stage_map = dict()
        for coord, square in self._map.items():
            next_stage_map[coord] = self._square_evolve(square, coord)
        self._map = next_stage_map
        return self._map

    def _square_evolve(self, square: str, coordinates: Coordinates) -> str:
        if square == self.FLOOR:
            return square
        occupied_adjacent = self._number_of_occupied_adjacent(coordinates)
        if square == self.FREE and occupied_adjacent == 0:
            return self.OCCUPIED
        if square == self.OCCUPIED and occupied_adjacent >= self.EMPTY_THRESHOLD:
            return self.FREE
        return square

    def _number_of_occupied_adjacent(self, coordinates: Coordinates) -> int:
        count_occupied = 0
        for seat in self._visible_seats(coordinates):
            if seat == self.OCCUPIED:
                count_occupied += 1
        return count_occupied

    def _visible_seats(self, coordinates: Coordinates) -> list[str]:
        adjacent_cells = [
            self._find_top_left(coordinates),
            self._find_top(coordinates),
            self._find_top_right(coordinates),
            self._find_right(coordinates),
            self._find_bottom_right(coordinates),
            self._find_bottom(coordinates),
            self._find_bottom_left(coordinates),
            self._find_left(coordinates),
        ]

        return list(map(self._square_at, filter(None, adjacent_cells)))

    @functools.lru_cache(None)
    def _find_top_left(self, coordinates: Coordinates) -> Coordinates | None:
        return self._find_with_delta(coordinates, (-1, -1))

    @functools.lru_cache(None)
    def _find_with_delta(
        self, coordinates: Coordinates, delta: tuple[int, int]
    ) -> Coordinates | None:
        other_coord = (coordinates[0] + delta[0], coordinates[1] + delta[1])
        try:
            self._square_at(other_coord)
        except KeyError:
            return None
        return other_coord

    @functools.lru_cache(None)
    def _find_top(self, coordinates: Coordinates) -> Coordinates | None:
        return self._find_with_delta(coordinates, (-1, 0))

    @functools.lru_cache(None)
    def _find_top_right(self, coordinates: Coordinates) -> Coordinates | None:
        return self._find_with_delta(coordinates, (-1, 1))

    @functools.lru_cache(None)
    def _find_right(self, coordinates: Coordinates) -> Coordinates | None:
        return self._find_with_delta(coordinates, (0, 1))

    @functools.lru_cache(None)
    def _find_bottom_right(self, coordinates: Coordinates) -> Coordinates | None:
        return self._find_with_delta(coordinates, (1, 1))

    @functools.lru_cache(None)
    def _find_bottom(self, coordinates: Coordinates) -> Coordinates | None:
        return self._find_with_delta(coordinates, (1, 0))

    @functools.lru_cache(None)
    def _find_bottom_left(self, coordinates: Coordinates) -> Coordinates | None:
        return self._find_with_delta(coordinates, (1, -1))

    @functools.lru_cache(None)
    def _find_left(self, coordinates: Coordinates) -> Coordinates | None:
        return self._find_with_delta(coordinates, (0, -1))


class SeatMapPart2(SeatMap):
    EMPTY_THRESHOLD = 5

    @functools.lru_cache(None)
    def _find_with_delta(
        self, coordinates: Coordinates, delta: tuple[int, int]
    ) -> Coordinates | None:
        other_coord = (coordinates[0] + delta[0], coordinates[1] + delta[1])
        try:
            other_square = self._square_at(other_coord)
            while other_square == self.FLOOR:
                other_coord = (other_coord[0] + delta[0], other_coord[1] + delta[1])
                other_square = self._square_at(other_coord)
        except KeyError:
            return None
        return other_coord


if __name__ == "__main__":
    main("inputs/day11-test1", 37, 26)
    main("inputs/day11", 2324, 2068)
