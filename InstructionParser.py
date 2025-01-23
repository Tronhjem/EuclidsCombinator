from InstructionMap import InstructionMap

class InstructionParser:
    def __init__(self, instruction_map: InstructionMap, parts: dict):
        self._instruction_map = instruction_map
        self._parts = parts

    def parse_instructions(self, instruction_text: str):
        line_count = 0
        for line in instruction_text:
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            line = line.lower()
            print(line)

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
                pass
                
            elif operation[0] == '[':
                pass
            elif operation[0] == '{':
                pass

            line_count += 1


#Testing code
parts = {}

ins_map = InstructionMap(parts)

with open('TestInstructions.txt', 'r') as file:
    instructions = file.readlines()

parser = InstructionParser(ins_map, parts)
parser.parse_instructions(instructions)

