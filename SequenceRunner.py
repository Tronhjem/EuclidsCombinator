from threading import Thread
# import psutil
# import os

from time import time as timenow
from MidiOutHandler import MidiOutHandler
from SequencePart import Part

class SequenceRunner(Thread):
    def __init__(self, bpm):
        super(SequenceRunner, self).__init__()
        # Set high priority for the process windows.
        # p = psutil.Process(os.getpid())
        # p.nice(psutil.REALTIME_PRIORITY_CLASS)

        self._running = True
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

        while self._running:
            nextStep = self.timeOfLastStep + self.interval
            if timenow() >= nextStep:
                for part in self.parts:
                    if part.shouldTrigger():
                        self.midiHandler.noteout(part.note, 100)

                self.timeOfLastStep = timenow()


    def shutdown(self):
        self._running = False