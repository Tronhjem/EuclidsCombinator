from EuclidSeq import EuclidSeq 
from SequenceRunner import SequenceRunner

from threading import Thread
from time import sleep, time as timenow


if __name__ == '__main__':
    seq = SequenceRunner(100)
    try:
        while True:
            sleep(1)

    except KeyboardInterrupt:
        print('')

    finally:
        seq.shutdown() # And kill it.
        seq.join()
        del seq

        print("Done")

