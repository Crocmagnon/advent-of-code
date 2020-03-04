NUMBER_OF_PARAMS_MAP = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
}

LAST_IS_RESULT_MAP = {
    1: True,
    2: True,
    3: True,
    4: False,
    5: False,
    6: False,
    7: True,
    8: True,
}


def get_value(program, args, param_modes, index):
    if param_modes[index] == 0:
        return program[args[index]]
    return args[index]


def parse_args(program, raw_args, param_modes, last_is_result=False):
    args = []
    limit = -1 if last_is_result else None
    for i, arg in enumerate(raw_args[:limit]):
        args.append(get_value(program, raw_args, param_modes, i))
    if last_is_result:
        args.append(raw_args[-1])
    return args


def compute(lst):
    program = lst.copy()

    pointer = 0
    while pointer < len(program):
        pointer_moved = False
        instruction = str(program[pointer])
        code = int(instruction[-2:])
        if code == 99:
            print("Halting due to code 99")
            return program

        number_of_params = NUMBER_OF_PARAMS_MAP[code]
        offset = number_of_params + 1
        param_modes = instruction[:-2]
        param_modes = param_modes.zfill(number_of_params)
        param_modes = list(map(int, reversed(param_modes)))
        raw_params = []
        for i in range(1, offset):
            raw_params.append(program[pointer + i])

        last_is_result = LAST_IS_RESULT_MAP[code]
        params = parse_args(program, raw_params, param_modes, last_is_result)

        if code == 1:
            # Addition
            program[params[2]] = params[0] + params[1]
        elif code == 2:
            # Multiplication
            program[params[2]] = params[0] * params[1]
        elif code == 3:
            # Input
            program[params[0]] = int(input(f"Input for instruction {pointer}\n> "))
        elif code == 4:
            # Output
            print(params[0])
        elif code == 5:
            # Jump if true
            if params[0] != 0:
                pointer = params[1]
                pointer_moved = True
        elif code == 6:
            # Jump if false
            if params[0] == 0:
                pointer = params[1]
                pointer_moved = True
        elif code == 7:
            # Less than
            if params[0] < params[1]:
                program[params[2]] = 1
            else:
                program[params[2]] = 0
        elif code == 8:
            # Equals
            if params[0] == params[1]:
                program[params[2]] = 1
            else:
                program[params[2]] = 0

        else:
            raise ValueError(f"Something bad happened, code={code}")

        if not pointer_moved:
            pointer += offset

    return program


if __name__ == "__main__":
    with open("inputs/day05") as f:
        compute(list(map(int, f.read().split(","))))
