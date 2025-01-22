from Instruction import InstructionSet, Instruction

class InstructionMap:
    def __init__(self, parts):
        self._instruction_map = {}
        self._parts = parts

    def get_instruction_set(self, instruction_set: str):
        instruction_set = instruction_set.replace(" ", "")

        if instruction_set in self._instruction_map:
            return self._instruction_map[instruction_set]
        else:

            self.build_instruction(instruction_set)
            if instruction_set in self._instruction_map:
                return self._instruction_map[instruction_set]

            print(f'No Instruction set found for {instruction_set}')

    def build_instruction(self, instruction: str):
        if instruction in self._instruction_map:
            return

        instruction = instruction.replace(" ", "")
        temp_name = f''
        parsed_instructions = []
        index = 0
        length = len(instruction)
        while index < length:
            char = instruction[index]
            if char != '&' and char != '^' and char != '|':
                char = instruction[index]
                temp_name += char

            else:
                parsed_instructions.append(temp_name)
                temp_name = f''
                parsed_instructions.append(char)

            index += 1

        parsed_instructions.append(temp_name)

        instruction_length = len(parsed_instructions)
        if (instruction_length - 1) % 2 == 0:
            instruction_set = InstructionSet()
            instruction_set.add_instruction(Instruction(parsed_instructions[0], '', self._parts))

            index = 1
            while index < instruction_length - 1:
                instruction_set.add_instruction(Instruction(parsed_instructions[index + 1], parsed_instructions[index], self._parts))
                index += 2

            self._instruction_map[instruction] = instruction_set

        else:
            print(f'Not enough instructions or uneven number in {instruction}')

