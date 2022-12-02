import pytest
from day11_seating import SeatMap


@pytest.fixture
def simple_map():
    return """L.L
L.L
.LL
"""


def test_adjacent_cells_center_simple_map(simple_map):
    seat_map = SeatMap(simple_map)
    adjacent = list(seat_map._visible_seats((1, 1)))
    assert adjacent == ["L", ".", "L", "L", "L", ".", "L", "L"]


def test_adjacent_cells_left_border_simple_map(simple_map):
    seat_map = SeatMap(simple_map)
    adjacent = list(seat_map._visible_seats((1, 0)))
    assert adjacent == ["L", ".", ".", "L", "."]


def test_adjacent_cells_top_left_corner_simple_map(simple_map):
    seat_map = SeatMap(simple_map)
    adjacent = list(seat_map._visible_seats((0, 0)))
    assert adjacent == [".", ".", "L"]
