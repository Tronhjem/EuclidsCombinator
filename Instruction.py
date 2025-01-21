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


class CombinationPair:
    def __init__(self, partOne, partTwo, logic):
        self.partOne = partOne
        self.partTwo = partTwo
        self.logic = logic
        

class Instruction:
    def __init__(self, a, b, logic, parts):
        self.parts = parts
        self.dictEntry = a+b
        self.parts[self.dictEntry] = 0

        if isinstance(self.parts[a], Part):
            self.process = self.CombineParts
        else:
            self.process = self.CombineTriggerAndPart
        
        self.a = a
        self.b = b
        self.logic = logic
        

    def processStep(self, step):
        step = self.process(step, self.a, self.b, self.logic)
        self.parts[self.dictEntry] = step
        return step
    

    def CombineParts(self, step, partOne, partTwo, logic):
        a = self.parts[partOne].shouldTrigger(step)
        b = self.parts[partTwo].shouldTrigger(step)
        return logic(a,b)


    def CombineTriggerAndPart(self, step, trigger, part, logic):
        return logic(self.parts[trigger], self.parts[part].shouldTrigger(step))




