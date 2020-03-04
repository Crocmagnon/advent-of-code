ZERO_PARAM_CODES = [99]
ONE_PARAM_CODES = [3, 4]
THREE_PARAMS_CODES = [1, 2]


def compute(lst):
    result = lst.copy()

    i = 0
    while i < len(result):
        first_instruction = str(result[i])
        code = int(first_instruction[-2:])
        param_modes = first_instruction[:-2]
        if code == 99:
            print("Halting due to code 99")
            return result
        if code in THREE_PARAMS_CODES:
            offset = 4
            param_modes = param_modes.zfill(offset - 1)
            param_modes_parsed = list(map(int, reversed(param_modes)))

            position1, position2 = result[i + 1], result[i + 2]
            if param_modes_parsed[0] == 0:
                item1 = result[position1]
            else:
                item1 = position1
            if param_modes_parsed[1] == 0:
                item2 = result[position2]
            else:
                item2 = position2
            result_index = result[i + 3]

            if code == 1:
                result[result_index] = item1 + item2
            elif code == 2:
                result[result_index] = item1 * item2

        elif code in ONE_PARAM_CODES:
            offset = 2
            param_mode = int(param_modes.zfill(offset - 1))
            position = result[i + 1]
            if code == 3:
                result[position] = int(input(f"Input for instruction {i}"))
            elif code == 4:
                if param_mode == 0:
                    res = result[position]
                else:
                    res = position
                print(res)

        else:
            raise ValueError(f"Something bad happened, code={code}")

        i += offset

    return result


if __name__ == "__main__":
    with open("inputs/day05") as f:
        compute(list(map(int, f.read().split(","))))
