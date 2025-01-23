from time import sleep
import os
import curses
from curses.textpad import Textbox, rectangle

from InstructionMap import InstructionMap
from ManualSequence import ManualSequence
from EuclidSeq import EuclidSeq

from Track import Track
from SequenceRunner import SequenceRunner




def render(stdscr, data):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Don't block I/O calls
    stdscr.timeout(100) # Refresh every 100 milliseconds

    my_list = [1, 2, 3, 4, 5]
    position = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Press 'q' to quit.")
        stdscr.addstr(1, 0, f"List: {my_list}")
        stdscr.addstr(2, 0, f"Position: {data.step}")

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break

        position = (position + 1) % len(my_list)
        # sleep(0.5)


if __name__ == '__main__':
    parts = {}
    instructions = InstructionMap(parts)

    # parts['A'] = ManualSequence([1, 0, 1, 0, 1, 0, 1, 0])
    # parts['Q'] = ManualSequence([1, 0, 1, 0, 1, 0, 1, 1, 1])

    # parts['B'] = EuclidSeq(4,7)

    # parts['C'] = EuclidSeq(1,5)

    # track = Track(36, 'A&B|C', instructions)
    # track2 = Track(42, 'B|C&Q', instructions)

    seq = SequenceRunner(100, instructions) # starts running here.

    try:
        curses.wrapper(render, seq)

    except KeyboardInterrupt:
        print('')

    finally:
        seq.shutdown() # kills it here
        seq.join()
        del seq

        print("Done")
