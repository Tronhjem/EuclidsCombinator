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


class Instruction:
    def __init__(self, part: str, operator: str, parts: dict):
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


class InstructionSet:
    """
    This is a list of instructions to be evaluated in the order they're added
    """
    def __init__(self):
        self._instructions = []

    def add_instruction(self, instruction):
        self._instructions.append(instruction)

    def evaluate_step(self, step):
        for_evaluation = self._instructions[0].evaluate_step(step)
        for x in range(1, len(self._instructions)):
            for_evaluation = self._instructions[x].evaluate_step(step, for_evaluation)

        return for_evaluation
