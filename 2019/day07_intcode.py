import itertools
from typing import List

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


class IntcodeOutput(Exception):
    def __init__(self, value):
        self.value = value


class Computer:
    def get_value(self, args, param_modes, index):
        if param_modes[index] == 0:
            return self.program[args[index]]
        return args[index]

    def parse_args(self, raw_args, param_modes, last_is_result=False):
        args = []
        limit = -1 if last_is_result else None
        for i, arg in enumerate(raw_args[:limit]):
            args.append(self.get_value(raw_args, param_modes, i))
        if last_is_result:
            args.append(raw_args[-1])
        return args

    def _move_pointer(self, position):
        self.pointer = position
        self.pointer_moved = True

    def _update_pointer(self):
        offset = self.get_offset()
        if not self.pointer_moved:
            self.pointer += offset
        self.pointer_moved = False

    def __init__(self, initial_program: list[int], inputs: list[int] = None):
        self.program = initial_program.copy()  # type: List[int]
        self.inputs = inputs.copy()  # type: List[int]
        self.pointer = 0
        self.pointer_moved = False

    def compute(self, additional_inputs: list[int] = None) -> int:
        if additional_inputs is None:
            additional_inputs = []
        self.inputs.extend(additional_inputs)

        while self.pointer < len(self.program):
            try:
                self.handle_operation()
            except IntcodeOutput as e:
                return e.value
            finally:
                self._update_pointer()

    def get_params(self):
        offset = self.get_offset()
        param_modes = self.get_instruction()[:-2]
        param_modes = param_modes.zfill(offset - 1)
        param_modes = list(map(int, reversed(param_modes)))
        raw_params = []
        for i in range(1, offset):
            raw_params.append(self.program[self.pointer + i])

        code = self.get_code()
        last_is_result = LAST_IS_RESULT_MAP[code]
        params = self.parse_args(raw_params, param_modes, last_is_result)
        return params

    def get_offset(self):
        code = self.get_code()
        number_of_params = NUMBER_OF_PARAMS_MAP[code]
        return number_of_params + 1

    def get_code(self):
        instruction = self.get_instruction()
        code = int(instruction[-2:])
        if code == 99:
            raise StopIteration
        return code

    def get_instruction(self):
        instruction = str(self.program[self.pointer])
        return instruction

    def handle_operation(self):
        code = self.get_code()
        params = self.get_params()
        if code == 1:
            self.handle_addition(params)
        elif code == 2:
            self.handle_multiplication(params)
        elif code == 3:
            self.handle_input(params)
        elif code == 4:
            # Output
            raise IntcodeOutput(params[0])
        elif code == 5:
            self.handle_jump_if_true(params)
        elif code == 6:
            self.handle_jump_if_false(params)
        elif code == 7:
            self.handle_less_than(params)
        elif code == 8:
            self.handle_equals(params)
        else:
            raise ValueError(f"Something bad happened, code={code}")

    def handle_addition(self, params):
        self.program[params[2]] = params[0] + params[1]

    def handle_multiplication(self, params):
        self.program[params[2]] = params[0] * params[1]

    def handle_input(self, params):
        self.program[params[0]] = int(self.inputs.pop(0))

    def handle_jump_if_true(self, params):
        if params[0] != 0:
            self._move_pointer(params[1])

    def handle_jump_if_false(self, params):
        if params[0] == 0:
            self._move_pointer(params[1])

    def handle_equals(self, params):
        if params[0] == params[1]:
            self.program[params[2]] = 1
        else:
            self.program[params[2]] = 0

    def handle_less_than(self, params):
        if params[0] < params[1]:
            self.program[params[2]] = 1
        else:
            self.program[params[2]] = 0


def main():
    with open("inputs/day07") as input_file:
        original_program = list(map(int, input_file.read().split(",")))
    values = set()
    for phase in itertools.permutations("56789"):
        amp1 = Computer(original_program, [int(phase[0])])
        amp2 = Computer(original_program, [int(phase[1])])
        amp3 = Computer(original_program, [int(phase[2])])
        amp4 = Computer(original_program, [int(phase[3])])
        amp5 = Computer(original_program, [int(phase[4])])
        signal = 0
        while True:
            try:
                signal = amp1.compute([signal])
                signal = amp2.compute([signal])
                signal = amp3.compute([signal])
                signal = amp4.compute([signal])
                signal = amp5.compute([signal])
            except StopIteration:
                values.add(signal)
                break

    print(max(values))


if __name__ == "__main__":
    main()
