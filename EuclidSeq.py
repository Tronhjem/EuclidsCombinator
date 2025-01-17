class EuclidSeq:
    def __init__(self, hits, length):
        self.hits = hits
        self.length = length
        self.sequence = []
        self.generateSequence() 

    def generateSequence(self):
        self.sequence = []
        count = self.length

        for x in range(self.length):
            if count >= self.length:
                self.sequence.append(1)
                count = count - self.length

            else:
                self.sequence.append(0)

            count = count + self.hits

    def combineAnd(self, a, b):
        return a & b

    def combineOr(self, a, b):
        return a | b

    def comebineXor(self, a, b):
        return a ^ b
    
    def combineSequence(self, s1, s2, operation):
        output = []
        length = max(len(s1), len(s2))
        for i in range(length):
            result = operation(s1[i % len(s1)], s2[i % len(s2)])
            output.append(result)
        
        return output

    def __and__(self, other):
        return self.combineSequence(self.sequence, other.sequence, self.combineAnd)

    def __or__(self, other):
        return self.combineSequence(self.sequence, other.sequence, self.combineOr)

    def __xor__(self, other):
        return self.combineSequence(self.sequence, other.sequence, self.comebineXor)


def PrintSequence():
    s1 = EuclidSeq(6, 15)
    s2 = EuclidSeq(8, 17)

    print(s1.sequence)
    print(s2.sequence)
    print("-----------------------------------")
