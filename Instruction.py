from Part import Part


def OR(a, b):
    return a | b


def AND(a, b):
    return a & b


def XOR(a, b):
    return a ^ b


def GetOperation(operationString):
    if operationString == '&':
        return AND
    if operationString == '|':
        return OR
    if operationString == '^':
        return XOR


class InstructionSet:
    def __init__(self):
        self._instructions = []

    def add_instruction(self, instruction):
        self._instructions.append(instruction)

    def evaluate_step(self, step):
        for_evaluation = self._instructions[0].evaluate_step(step)
        for x in range(1, len(self._instructions)):
            for_evaluation = self._instructions[x].evaluate_step(step, for_evaluation)

        return for_evaluation


class Instruction:
    def __init__(self, part, operator, parts):
        self.parts = parts
        self.dictEntry = part + operator

        self.part_name = part
        self.part = self.parts[part]
        if operator is not None:
            self.operation = GetOperation(operator)

    def evaluate_step(self, step, evaluate_against = -1):
        if self.operation is not None and evaluate_against != -1:
            return self.operation(evaluate_against, self.part.evaluate_step(step))
        else:
            return self.part.evaluate_step(step)


class InstructionMap:
    def __init__(self, parts):
        self._instruction_map = {}
        self._parts = parts

    def get_instruction_set(self, instruction_set):
        instruction_set = instruction_set.replace(" ", "")
        if instruction_set in self._instruction_map:
            return self._instruction_map[instruction_set]
        else:
            print(f'No Instruction set found for {instruction_set}')

    def build_instruction(self, instruction_string):
        if instruction_string in self._instruction_map:
            return

        instruction_string = instruction_string.replace(" ", "")
        temp_name = f''
        parsed_instructions = []
        index = 0
        length = len(instruction_string)
        while index < length:
            char = instruction_string[index]
            if char != '&' and char != '^' and char != '|':
                char = instruction_string[index]
                temp_name += char

            else:
                parsed_instructions.append(temp_name)
                temp_name = f''
                parsed_instructions.append(char)

            index += 1

        parsed_instructions.append(temp_name)

        instruction_length = len(parsed_instructions)
        if (instruction_length - 1) % 2 != 0:
            print(f'Not enough instructions or uneven number in {instruction_string}')

        else:
            instruction_set = InstructionSet()
            instruction_set.add_instruction(Instruction(parsed_instructions[0], '', self._parts))

            index = 1
            while index < instruction_length - 1:
                instruction_set.add_instruction(Instruction(parsed_instructions[index + 1], parsed_instructions[index], self._parts))
                index += 2

            self._instruction_map[instruction_string] = instruction_set


if __name__ == "__main__":
    print("@@@@")
    parts_map = {}
    instructions_map = InstructionMap(parts_map)

    parts_map['Foo'] = Part()
    parts_map['Foo'].set_sequence([1, 0, 1, 0, 1, 0, 1])

    parts_map['Bar'] = Part()
    parts_map['Bar'].set_sequence([1, 1, 1, 0, 1, 0, 0, 0, 1, 1])

    parts_map['CSomething'] = Part()
    parts_map['CSomething'].set_sequence([1, 0, 0, 1])

    instructions_map.build_instruction('Foo | Bar')
    print(instructions_map.get_instruction_set('Foo|Bar').evaluate_step(1))
