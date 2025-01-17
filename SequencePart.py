class Part:
    def __init__(self, note, seq):
        self.sequence = seq
        self.counter = 0
        self.note = note
    
    
    def shouldTrigger(self):
        trigger = self.sequence[self.counter] == 1
        self.counter = (self.counter + 1) % len(self.sequence)
        return trigger 
    

    def setEuclidSequence(self, euclid):
        self.euclid = euclid
        self.sequence = self.euclid.sequence

