from InstructionMap import InstructionMap
from EuclidSeq import EuclidSeq
from ManualSequence import ManualSequence
from Track import Track

class InstructionParser:
    def __init__(self, instruction_map: InstructionMap, parts: dict, instructions):
        self._instruction_map = instruction_map
        self._parts = parts
        self._instructions = instructions

    def update(self, instructions):
        self._instructions = instructions
        self._instruction_map.clear()
        self._parts.clear()
        self._parts['tracks'] = []
        self.parse_instructions(self._instructions)

    def parse_instructions(self, instruction_text: str):
        line_count = 0
        for line in instruction_text:
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            line = line.lower()

            var_name = f''
            index = 0 
            length = len(line)
            temp_char = ''
            while index < length:
                temp_char = line[index]
                if temp_char == '=':
                    break

                elif temp_char != '=':
                    var_name += temp_char
                    index += 1
            
            index += 1
            operation = line[index:]
            temp_char = ''

            if index == length:
                print(f'No assignment to variable on line {line_count}: {index}')
                continue
            if len(operation) < 1:
                print(f'no operation for line {line_count}: {line} ')
                continue

            if operation[0] == '(':
                hit = int(operation[1])
                length = int(operation[3])
                self._parts[var_name] = EuclidSeq(hit, length)
                
            elif operation[0] == '[':
                end_index = operation.index(']')
                operation_set = operation[1:end_index].split(',')
                if len(operation_set) > 0:
                    operation_set = [int(x) for x in operation_set]
                    self._parts[var_name] = ManualSequence(operation_set)

            elif operation[0] == '{':
                operation_set = operation[1:]
                operation_set = operation_set.replace('}','')
                commands = operation_set.split(',')
                if len(commands) > 1 and len(commands) < 3:
                    self._parts[var_name] = Track(int(commands[0]), commands[1], self._instruction_map)
                    self._parts['tracks'].append(self._parts[var_name])
                else:
                    print(f'Error in commands for tracks on line {line_count}: {line}')
                    print('Track expects 2 commands. e.g. t1 = {32, A|B}')

            line_count += 1


