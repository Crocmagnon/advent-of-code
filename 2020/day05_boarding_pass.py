def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    found_part_1 = 0
    seat_ids = set()
    with open(filename) as f:
        for boarding_pass in f:
            id_ = seat_id(boarding_pass)
            seat_ids.add(id_)
            if id_ > found_part_1:
                found_part_1 = id_

    print(f"1. Found {found_part_1}")
    if expected_part_1:
        assert found_part_1 == expected_part_1

    sorted_ids = sorted(seat_ids)
    current = sorted_ids[0]
    found_part_2 = 0
    for id_ in sorted_ids:
        if id_ != current:
            found_part_2 = current
            break
        current += 1

    print(f"2. Found {found_part_2}")
    if expected_part_2:
        assert found_part_2 == expected_part_2


def seat_id(boarding_pass: str):
    boarding_pass = boarding_pass.strip()
    binary = (
        boarding_pass.replace("F", "0")
        .replace("B", "1")
        .replace("R", "1")
        .replace("L", "0")
    )
    return int(binary, 2)


if __name__ == "__main__":
    main("inputs/day05-test1", 567, 566)
    main("inputs/day05-test2", 119)
    main("inputs/day05-test3", 820)
    main("inputs/day05-test4", 820)
    main("inputs/day05")
