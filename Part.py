class Part:
    def __init__(self):
        self._sequence = []
        self.length = len(self._sequence)
        self.euclid = None

    def evaluate_step(self, step):
        trigger = self._sequence[step % self.length] == 1
        return trigger

    def set_euclid_sequence(self, euclid):
        self.euclid = euclid
        self._sequence = self.euclid._sequence
        self.length = len(self._sequence)

    def set_sequence(self, sequence):
        self._sequence = sequence
        self.length = len(self._sequence)
