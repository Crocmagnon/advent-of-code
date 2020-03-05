import itertools
from typing import List, Union

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


class Computer:
    @staticmethod
    def get_value(program, args, param_modes, index):
        if param_modes[index] == 0:
            return program[args[index]]
        return args[index]

    @staticmethod
    def parse_args(program, raw_args, param_modes, last_is_result=False):
        args = []
        limit = -1 if last_is_result else None
        for i, arg in enumerate(raw_args[:limit]):
            args.append(Computer.get_value(program, raw_args, param_modes, i))
        if last_is_result:
            args.append(raw_args[-1])
        return args

    def __init__(self, initial_program: List[int], inputs: List[int] = None):
        self.program = initial_program.copy()  # type: List[int]
        self.inputs = inputs.copy()  # type: List[int]

    def compute(self, inputs: List[int] = None) -> Union[int, None]:
        if inputs is None:
            inputs = []
        self.inputs.extend(inputs)

        pointer = 0
        while pointer < len(self.program):
            pointer_moved = False
            instruction = str(self.program[pointer])
            code = int(instruction[-2:])
            if code == 99:
                raise

            number_of_params = NUMBER_OF_PARAMS_MAP[code]
            offset = number_of_params + 1
            param_modes = instruction[:-2]
            param_modes = param_modes.zfill(number_of_params)
            param_modes = list(map(int, reversed(param_modes)))
            raw_params = []
            for i in range(1, offset):
                raw_params.append(self.program[pointer + i])

            last_is_result = LAST_IS_RESULT_MAP[code]
            params = self.parse_args(
                self.program, raw_params, param_modes, last_is_result
            )

            if code == 1:
                # Addition
                self.program[params[2]] = params[0] + params[1]
            elif code == 2:
                # Multiplication
                self.program[params[2]] = params[0] * params[1]
            elif code == 3:
                # Input
                try:
                    input_value = int(self.inputs.pop(0))
                except IndexError:
                    input_value = int(input(f"Input for instruction {pointer}\n> "))
                self.program[params[0]] = input_value
            elif code == 4:
                # Output
                return params[0]
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
                    self.program[params[2]] = 1
                else:
                    self.program[params[2]] = 0
            elif code == 8:
                # Equals
                if params[0] == params[1]:
                    self.program[params[2]] = 1
                else:
                    self.program[params[2]] = 0

            else:
                raise ValueError(f"Something bad happened, code={code}")

            if not pointer_moved:
                pointer += offset


def main():
    with open("inputs/day07") as input_file:
        original_program = list(map(int, input_file.read().split(",")))
    values = set()
    for phase in itertools.permutations("01234"):
        amp1 = Computer(original_program, [int(phase[0])]).compute([0])
        amp2 = Computer(original_program, [int(phase[1])]).compute([amp1])
        amp3 = Computer(original_program, [int(phase[2])]).compute([amp2])
        amp4 = Computer(original_program, [int(phase[3])]).compute([amp3])
        amp5 = Computer(original_program, [int(phase[4])]).compute([amp4])
        values.add(amp5)

    print(max(values))


if __name__ == "__main__":
    main()
