from threading import Thread
# import psutil
# import os

from time import time as timenow
from MidiOutHandler import MidiOutHandler

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

        self.tracks = []

        self.start()


    def addTrack(self, part):
        self.tracks.append(part)


    def run(self):
        self.timeOfLastStep = timenow()

        while self._running:
            nextStep = self.timeOfLastStep + self.interval
            if timenow() >= nextStep:
                self.step += 1
                for track in self.tracks:
                    if track.evaluate_next_step():
                        self.midiHandler.noteout(track._note, 100)

                self.timeOfLastStep = timenow()


    def shutdown(self):
        self._running = False