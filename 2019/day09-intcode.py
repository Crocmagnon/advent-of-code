import itertools
from collections import defaultdict
from typing import List, Union

RELATIVE_MODE = 2
POSITION_MODE = 0
VALUE_MODE = 1
NUMBER_OF_PARAMS_MAP = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 1,
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
    9: False,
}


class IntcodeOutput(Exception):
    def __init__(self, value):
        self.value = value


class Computer:
    def __init__(self, initial_program: List[int], inputs: List[int] = None):
        self.program = defaultdict(int, enumerate(initial_program))
        if inputs is None:
            inputs = []
        self.inputs = inputs.copy()  # type: List[int]
        self.pointer = 0
        self.pointer_moved = False
        self.relative_base = 0

    def get_value(self, args, param_modes, index):
        if param_modes[index] == RELATIVE_MODE:
            return self.program[self.relative_base + args[index]]
        if param_modes[index] == POSITION_MODE:
            return self.program[args[index]]
        return args[index]

    def parse_args(self, raw_args, param_modes, code):
        args = []
        last_is_result = LAST_IS_RESULT_MAP[code]
        limit = -1 if last_is_result else None
        for i, arg in enumerate(raw_args[:limit]):
            args.append(self.get_value(raw_args, param_modes, i))
        if last_is_result:
            if param_modes[-1] == RELATIVE_MODE:
                args.append(raw_args[-1] + self.relative_base)
            else:
                args.append(raw_args[-1])
        return args

    def _move_pointer(self, position):
        self.pointer = position
        self.pointer_moved = True

    def _update_pointer(self, code):
        offset = self.get_offset(code)
        if not self.pointer_moved:
            self.pointer += offset
        self.pointer_moved = False

    def compute(self, additional_inputs: List[int] = None) -> int:
        if additional_inputs is None:
            additional_inputs = []
        self.inputs.extend(additional_inputs)

        while self.pointer < len(self.program):
            code = self.get_code()
            try:
                self.handle_operation(code)
            except IntcodeOutput as e:
                print(e.value)
            finally:
                self._update_pointer(code)

    def get_params(self, code):
        offset = self.get_offset(code)
        param_modes = self.get_instruction()[:-2]
        param_modes = param_modes.zfill(offset - 1)
        param_modes = list(map(int, reversed(param_modes)))
        raw_params = []
        for i in range(1, offset):
            raw_params.append(self.program[self.pointer + i])

        params = self.parse_args(raw_params, param_modes, code)
        return params

    def get_offset(self, code):
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

    def handle_operation(self, code):
        params = self.get_params(code)
        if code == 1:
            self.handle_addition(params)
        elif code == 2:
            self.handle_multiplication(params)
        elif code == 3:
            self.handle_input(params)
        elif code == 4:
            self.handle_output(params)
        elif code == 5:
            self.handle_jump_if_true(params)
        elif code == 6:
            self.handle_jump_if_false(params)
        elif code == 7:
            self.handle_less_than(params)
        elif code == 8:
            self.handle_equals(params)
        elif code == 9:
            self.handle_adjust_relative_base(params)
        else:
            raise ValueError(f"Something bad happened, code={code}")

    def handle_addition(self, params):
        self.program[params[2]] = params[0] + params[1]

    def handle_multiplication(self, params):
        self.program[params[2]] = params[0] * params[1]

    def handle_input(self, params):
        self.program[params[0]] = int(self.inputs.pop(0))

    def handle_output(self, params):
        raise IntcodeOutput(params[0])

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

    def handle_adjust_relative_base(self, params):
        self.relative_base += params[0]


def main():
    with open("inputs/day09") as input_file:
        original_program = list(map(int, input_file.read().split(",")))
    computer = Computer(original_program)
    try:
        result = computer.compute([1])
        print(result)
    except StopIteration:
        pass


if __name__ == "__main__":
    main()
