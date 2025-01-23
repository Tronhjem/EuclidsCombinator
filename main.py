from time import sleep
import os
import math

import curses
from curses.textpad import Textbox, rectangle

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from InstructionMap import InstructionMap
from InstructionParser import InstructionParser
from SequenceRunner import SequenceRunner


def render(stdscr, data):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Don't block I/O calls
    stdscr.timeout(25)  # Refresh every 25 milliseconds

    cursor =  ['_', '_', '_', '_', '_', '_', '_', '_']
    tempDisplay =  ['', '', '', '', '', '', '', '']
    currentStep = 0

    while True:
        # stdscr.clear()
        stdscr.addstr(0, 0, "Press 'q' to quit.")
        stdscr.addstr(1, 0, "")

        cursor[currentStep] = '_' 
        currentStep = data._step % 8
        cursor[currentStep] = '@'
        stdscr.addstr(2, 0, f"Position: {cursor}")

        start = math.floor(data._step / 8) * 8
        index = 3
        for track in data._parts['tracks']:
            temp_index = 0
            for x in range(start, start + 8):
                sign = '_'
                if track.querry_step(x):
                    sign = 'X'
                tempDisplay[temp_index] = sign
                temp_index += 1

            stdscr.addstr(index, 0, f"Track:    {tempDisplay}")
            index += 1

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break


class MyHandler(FileSystemEventHandler):
    def __init__(self, file_to_watch, update_function):
        super().__init__()
        self._file_to_watch = file_to_watch
        self._update_callback = update_function
    
    def on_modified(self, event):
        if event.src_path == self._file_to_watch:
            self._update_callback()


if __name__ == '__main__':
    parts = {}
    parts['tracks'] = []

    script_path = os.path.dirname(os.path.abspath(__file__))
    instructions_file = os.path.join(script_path, 'TestInstructions.txt')

    with open(instructions_file, 'r') as file:
        instructions = file.readlines()

    instructions_map = InstructionMap(parts)
    instruction_parser = InstructionParser(instructions_map, parts, instructions)
    instruction_parser.parse_instructions(instructions)
    seq = SequenceRunner(100, instructions_map, parts) # starts running here.

    event_handler = MyHandler(instructions_file, instruction_parser.update)
    observer = Observer()
    observer.schedule(event_handler, path=script_path, recursive=False)
    observer.start()

    try:
        curses.wrapper(render, seq)
        observer.stop()
        seq.shutdown()

    except KeyboardInterrupt:
        observer.stop()
        seq.shutdown()

    finally:
        seq.join()
        observer.join()

        print("Done")
