import curses
from watchdog.observers import Observer
import traceback

from InstructionMap import InstructionMap
from InstructionParser import InstructionParser
from SequenceRunner import SequenceRunner
from FileHandler import FileHandler
from RenderConsole import render


if __name__ == '__main__':
    parts = {}
    parts['tracks'] = []

    file_handler = FileHandler(None)
    instructions = file_handler.read_file()

    instructions_map = InstructionMap(parts)
    instruction_parser = InstructionParser(instructions_map, parts, instructions)
    instruction_parser.parse_instructions(instructions)
    file_handler.set_update_callback(instruction_parser.update)
    seq = SequenceRunner(100, instructions_map, parts) # sequence starts thread.

    #observer for updating sequences when text file is edited.
    observer = Observer()
    observer.schedule(file_handler, path=file_handler.script_path, recursive=False)
    observer.start()

    try:
        curses.wrapper(render, seq, file_handler)
        observer.stop()
        seq.shutdown()

    except KeyboardInterrupt:
        observer.stop()
        seq.shutdown()

    except Exception as e:
        print("Exception occurred:")
        traceback.print_exc()
        observer.stop()
        seq.shutdown()

    finally:
        seq.join()
        observer.join()

        print("Done")
