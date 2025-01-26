import math
import curses
from curses.textpad import Textbox, rectangle

def render(stdscr, data, text_file_handler):
    # curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Don't block I/O calls
    stdscr.timeout(20)  # Refresh every 25 milliseconds

    cursor =  ['_', '_', '_', '_', '_', '_', '_', '_']
    tempDisplay =  ['', '', '', '', '', '', '', '']
    currentStep = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 10, "Press 'q' to quit.")
        stdscr.addstr(1, 10, "Press 'e' to edit sequences")
        stdscr.addstr(2, 10, "Press 'ctl-g' to exit editing")

        win_height = 13
        win_width  = 45

        index = 4
        for line in text_file_handler.instructions:
            stdscr.addstr(index, 3, line)
            index += 1

        editwin = curses.newwin(win_height, win_width, 4, 2)
        rectangle(stdscr, 3, 1, win_height + 3, win_width + 5)

        cursor[currentStep] = '_' 
        currentStep = data._step % 8
        cursor[currentStep] = '@'

        stdscr.addstr(17, 1, f"     {cursor}")
        index = 18
        start = math.floor(data._step / 8) * 8

        if 'tracks' in data._parts:
            for track in data._parts['tracks']:
                temp_index = 0
                for x in range(start, start + 8):
                    sign = '_'
                    if track.querry_step(x):
                        sign = 'X'
                    tempDisplay[temp_index] = sign
                    temp_index += 1

                stdscr.addstr(index, 1, f"     {tempDisplay}")
                index += 1

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == ord('p'):
            data.toggle_pause()
        if key == ord('e'):

            index = 0
            for line in text_file_handler.instructions:
                editwin.addstr(index, 0, line)  # Set initial text here
                index += 1

            box = Textbox(editwin)
            box.edit()
            message = box.gather()
            
            text_file_handler.write_to_file(message)
