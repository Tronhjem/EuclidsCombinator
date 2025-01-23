from Part import Part

class ManualSequence(Part):
    def __init__(self, sequence: list):
        super().__init__()
        self._sequence = list(sequence)
        self._length = len(self._sequence)
