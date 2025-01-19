from time import sleep
from SequenceRunner import SequenceRunner

if __name__ == '__main__':
    seq = SequenceRunner(100) # starts running here. 
    
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
