from day10_adapter_array import solve_part_2


def test_only_one_path():
    assert solve_part_2([0, 1]) == 1


def test_one_long_paths():
    assert solve_part_2([0, 1, 4, 7]) == 1


def test_two_paths():
    assert solve_part_2([0, 1, 2]) == 2
