class Part:
    def __init__(self):
        self.sequence = []
        self.length = len(self.sequence)
        self.euclid = None

    
    def shouldTrigger(self, position):
        trigger = self.sequence[position % self.length] == 1
        return trigger 
    

    def setEuclidSequence(self, euclid):
        self.euclid = euclid
        self.sequence = self.euclid.sequence
        self.length = len(self.sequence)


    def setSequence(self, sequence):
        self.sequence = sequence
        self.length = len(self.sequence)

