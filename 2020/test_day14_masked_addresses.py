import pytest

from day14_docking import ProgramPart2


@pytest.fixture
def program():
    return ProgramPart2([])


def test_no_floating(program):
    program.mask = "0" * 36
    assert list(program.get_masked_addresses(8)) == [8]


def test_last_floating(program):
    program.mask = "0" * 35 + "X"
    assert list(program.get_masked_addresses(8)) == [8, 9]


def test_second_to_last_floating(program):
    program.mask = "0" * 34 + "X0"
    assert list(program.get_masked_addresses(8)) == [8, 10]


def test_last_two_floating(program):
    program.mask = "0" * 34 + "XX"
    assert list(program.get_masked_addresses(8)) == [8, 9, 10, 11]


def test_one_bit_replacement(program):
    program.mask = "0" * 35 + "1"
    assert list(program.get_masked_addresses(8)) == [9]


def test_two_bits_replacement(program):
    program.mask = "0" * 34 + "11"
    assert list(program.get_masked_addresses(8)) == [11]
