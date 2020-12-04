import re
from typing import List


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        passports = f.read().strip().split("\n\n")  # type: List[str]

    counter_part_1 = 0
    counter_part_2 = 0
    fields_validation = {
        "byr": validate_byr,
        "iyr": validate_iyr,
        "eyr": validate_eyr,
        "hgt": validate_hgt,
        "hcl": validate_hcl,
        "ecl": validate_ecl,
        "pid": validate_pid,
    }
    for passport_str in passports:
        passport_data = extract_passport_data(passport_str)
        if is_valid_for_part_1(passport_data, fields_validation):
            counter_part_1 += 1
        if is_valid_for_part_2(passport_data, fields_validation):
            counter_part_2 += 1

    print(f"1. Found {counter_part_1} valid passports")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    print(f"2. Found {counter_part_2} valid passports")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


def extract_passport_data(passport):
    return dict([tuple(field.split(":")) for field in passport.split()])


def is_valid_for_part_1(passport_data, fields_validation):
    return (fields_validation.keys() - passport_data.keys()) == set()


def is_valid_for_part_2(passport_data, fields_validation):
    try:
        for validator in fields_validation.values():
            validator(passport_data)
    except (KeyError, ValueError, TypeError, AssertionError):
        return False

    return True


def validate_byr(passport_data):
    assert_int_between(passport_data["byr"], 1920, 2002)


def validate_iyr(passport_data):
    assert_int_between(passport_data["iyr"], 2010, 2020)


def validate_eyr(passport_data):
    assert_int_between(passport_data["eyr"], 2020, 2030)


def assert_int_between(value, low, high):
    value = int(value)
    assert low <= value <= high


def validate_hgt(passport_data):
    hgt = passport_data["hgt"]
    reg = re.compile(r"^(?P<value>\d+)(?P<unit>cm|in)$")
    assert (match := reg.match(hgt))
    groups = match.groupdict()
    value = int(groups["value"])
    unit = groups["unit"]
    if unit == "in":
        assert 59 <= value <= 76
    elif unit == "cm":
        assert 150 <= value <= 193
    else:
        raise AssertionError("No unit found")


def validate_hcl(passport_data):
    hcl = passport_data["hcl"]
    reg = re.compile(r"^#[0-9a-f]{6}$")
    assert reg.match(hcl)


def validate_ecl(passport_data):
    ecl = passport_data.get("ecl")
    assert ecl in "amb blu brn gry grn hzl oth".split()


def validate_pid(passport_data):
    pid = passport_data["pid"]
    reg = re.compile(r"^\d{9}$")
    assert reg.match(pid)


if __name__ == "__main__":
    main("inputs/day04-tests-1", 2)
    main("inputs/day04-tests-2", 4, 0)
    main("inputs/day04-tests-3", 4, 4)
    main("inputs/day04", 170, 103)
