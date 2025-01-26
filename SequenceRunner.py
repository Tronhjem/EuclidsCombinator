from threading import Thread
from time import time as timenow
from time import sleep
# import psutil

from InstructionMap import InstructionMap

class SequenceRunner(Thread):
    def __init__(self, bpm, instruction_map: InstructionMap, parts, midi_handler):
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

        self._midiHandler = midi_handler

        self._instruction_map = instruction_map
        self._parts = parts
        self._is_paused = False

        self.start()


    def addTrack(self, part):
        self._tracks.append(part)

    def toggle_pause(self):
        self._is_paused = not self._is_paused
        print()

    def run(self):
        self._timeOfLastStep = timenow()

        while self._running:
            if self._is_paused:
                continue

            nextStep = self._timeOfLastStep + self._interval
            if timenow() >= nextStep:
                self._step += 1
                if 'tracks' in self._parts:
                    for track in self._parts['tracks']:
                        if track.evaluate_next_step():
                            self._midiHandler.noteout(track._note, 100)

                self._timeOfLastStep = timenow()

        print('Shutting down seq')
        del self._midiHandler

    def shutdown(self):
        self._running = False