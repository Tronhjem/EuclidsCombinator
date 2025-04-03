from Part import Part

class EuclidSeq(Part):
    def __init__(self, hits, length):
        super().__init__()
        self.hits = hits
        self._length = length
        self._sequence = [0] * length
        self.generate_sequence() 

    def generate_sequence(self):
        count = self._length

        for x in range(self._length):
            if count >= self._length:
                self._sequence[x] = 1
                count = count - self._length

            else:
                self._sequence[x] = 0

            count = count + self.hits

    # def __and__(self, other):
    #     return self.combineSequence(self.sequence, other._sequence, self.combineAnd)

    # def __or__(self, other):
    #     return self.combineSequence(self.sequence, other._sequence, self.combineOr)

    # def __xor__(self, other):
    #     return self.combineSequence(self.sequence, other._sequence, self.comebineXor)
