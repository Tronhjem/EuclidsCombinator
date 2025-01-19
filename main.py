from time import sleep
from Part import Part
from Track import Track
from SequenceRunner import SequenceRunner

parts = {}


if __name__ == '__main__':
    parts['A'] = Part()
    parts['A'].setSequence([1,0,1,0,1,0,1])

    parts['B'] = Part()
    parts['B'].setSequence([1,0,1,0,1,0,0,0, 1, 1])

    parts['C'] = Part()
    parts['C'].setSequence([1,0,0,1])

    track = Track(36, 'A&B|C', parts)
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
