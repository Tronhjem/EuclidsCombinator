from time import sleep

from Instruction import InstructionMap
from Part import Part
from Track import Track
from SequenceRunner import SequenceRunner

parts = {}
instructions = InstructionMap(parts)


if __name__ == '__main__':
    parts['A'] = Part()
    parts['A'].set_sequence([1, 0, 1, 0, 1, 0, 1])

    parts['B'] = Part()
    parts['B'].set_sequence([1, 0, 1, 0, 1, 0, 0, 0, 1, 1])

    parts['C'] = Part()
    parts['C'].set_sequence([1, 0, 0, 1])

    track = Track(36, 'A&B|C', instructions)

    seq = SequenceRunner(100) # starts running here.
    seq.addTrack(track)

    try:
        while True:
            sleep(1)

    except KeyboardInterrupt:
        print('')

    finally:
        seq.shutdown() # kills it here
        seq.join()
        del seq

        print("Done")
