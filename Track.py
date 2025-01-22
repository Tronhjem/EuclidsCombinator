from Instruction import InstructionMap


class Track:
    def __init__(self, note, instructions: str, instruction_map: InstructionMap):
        self._counter = 0
        self._note = note
        self._instruction_map = instruction_map
        self._instruction_set = self._instruction_map.get_instruction_set(instructions)

    def evaluate_next_step(self):
        evaluated_step = self._instruction_set.evaluate_step(self._counter)
        self._counter += 1
        return evaluated_step
