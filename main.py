from sequence import Sequence 
from MidiSequencer import MidiExample

from threading import Thread
from time import sleep, time as timenow


class Part:
    def __init__(self):
        self.sequence = []
        self.note = 64


class SequenceRunner(Thread):
    def __init__(self):
        super(SequenceRunner, self).__init__()

        self.running = True

        self.parts = []
        self.start()


    def run(self):
        while self.running:
            print()


    def shutdown(self):
        self.running = False
        

def PrintSequence():
    s1 = Sequence(6, 15)
    s2 = Sequence(8, 17)

    print(s1.sequence)
    print(s2.sequence)
    print("-----------------------------------")


if __name__ == '__main__':

