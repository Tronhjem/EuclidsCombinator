from sequence import Sequence 
from MidiOutHandler import MidiOutHandler

from threading import Thread
from time import sleep, time as timenow


class Part:
    def __init__(self, note, seq):
        self.sequence = seq
        self.counter = 0
        self.note = note
    
    def shouldTrigger(self):
        trigger = self.sequence[self.counter] == 1
        self.counter = (self.counter + 1) % len(self.sequence)
        return trigger 


class SequenceRunner(Thread):
    def __init__(self, bpm):
        super(SequenceRunner, self).__init__()

        self.running = True
        self.bpm = bpm
        self.beatDivision = 4.
        self.interval = 60. / (float(bpm) * self.beatDivision)

        self.step = 0
        self.timeOfLastStep = 0
        self.timeStart = 0

        self.midiHandler = MidiOutHandler()

        self.parts = []
        self.parts.append(Part(36, [1, 0, 1, 0]))
        self.parts.append(Part(38, [0, 0, 1, 0]))

        print('Running Sequence... press ctl-c to stop')
        self.start()


    def addPart(self, part):
        self.parts.append(part)


    def run(self):
        self.timeOfLastStep = timenow()

        while self.running:
            nextStep = self.timeOfLastStep + self.interval
            if timenow() >= nextStep:
                for part in self.parts:
                    if part.shouldTrigger():
                        self.midiHandler.noteout(part.note, 100)

                self.timeOfLastStep = timenow()


    def shutdown(self):
        self.running = False
        

if __name__ == '__main__':
    seq = SequenceRunner(100)
    try:
        while True:
            sleep(1)

    except KeyboardInterrupt:
        print('')

    finally:
        seq.shutdown() # And kill it.
        seq.join()
        del seq

        print("Done")

