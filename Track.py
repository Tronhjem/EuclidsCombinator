from Instruction import Instruction, GetOperation

class Track:
    def __init__(self, note, instructions, parts):
        self.counter = 0
        self.note = note
        self.instructions = instructions
        self.intructionSteps = []
        self.parts = parts

        self.buildInstructions()


    def buildInstructions(self):
        # build instructions should happen in another place where 
        # when parts added we add them to a dict.
        # when combinations happen we add them as well to the dict so they can be resused. 

        # an instruction set could be a class with bound referneces to the parts in the dict 
        # and then querried from here.

        tempName = f''
        operations = []
        index = 0
        length = len(self.instructions)
        while index < length:
            char = self.instructions[index]
            if char != '&' and char != '^' and char != '|':
                char = self.instructions[index]
                tempName += char

            else:
                operations.append(tempName)
                tempName = f''
                operations.append(char)

            index += 1

        operations.append(tempName)

        instructionLength = len(operations)
        if instructionLength < 3 or (instructionLength - 3) % 2 != 0:
            print(f'Not enough instructions or uneven number in {self.instructions}')

        else:
            # here we can just take the first part and get the result. 
            # from there we parse then in pairs, like operator and part, etc.
            # if we only have one part we only need the result and else we always have an operator and pair part.

            operation = GetOperation(operations[1])
            self.AddInstruction(Instruction(operations[0], operations[2], operation, self.parts))
            instructionIndex = 1
            index = 3

            while index < instructionLength - 1:
                previousName = self.intructionSteps[instructionIndex - 1].dictEntry
                partToCombine = operations[index + 1]
                operation = GetOperation(operations[index])

                self.AddInstruction(Instruction(previousName, partToCombine, operation, self.parts))
                instructionIndex += 1
                index += 2


    def AddInstruction(self, instruction):
        self.intructionSteps.append(instruction)


    def shouldTrigger(self):
        temp = 0
        for instruction in self.intructionSteps:
            temp = instruction.processStep(self.counter)

        self.counter += 1
        return temp
