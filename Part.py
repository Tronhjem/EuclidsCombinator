class Part:
    def __init__(self):
        self._sequence = []
        self._length = 0

    def evaluate_step(self, step):
        trigger = self._sequence[step % self._length] == 1
        return trigger
