from threading import Thread
from time import time as timenow
# import psutil

from InstructionMap import InstructionMap
from MidiOutHandler import MidiOutHandler

class SequenceRunner(Thread):
    def __init__(self, bpm, instruction_map: InstructionMap):
        super(SequenceRunner, self).__init__()
        # Set high priority for the process windows.
        # p = psutil.Process(os.getpid())
        # p.nice(psutil.REALTIME_PRIORITY_CLASS)

        self._running = True
        self._bpm = bpm
        self._beatDivision = 4.
        self._interval = 60. / (float(bpm) * self._beatDivision)

        self._step = 0
        self._timeOfLastStep = 0
        self._timeStart = 0

        self._midiHandler = MidiOutHandler()

        self._instruction_map = instruction_map
        self._tracks = []

        self.start()


    def addTrack(self, part):
        self._tracks.append(part)


    def run(self):
        self._timeOfLastStep = timenow()

        while self._running:
            nextStep = self._timeOfLastStep + self._interval
            if timenow() >= nextStep:
                self._step += 1
                for track in self._tracks:
                    if track.evaluate_next_step():
                        self._midiHandler.noteout(track._note, 100)

                self._timeOfLastStep = timenow()

        del self._midiHandler

    def shutdown(self):
        self._running = False