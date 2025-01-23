
This is a sequencer that uses sequences generated as euclidean sequences or manually typed, and combines these into poly rythmical sequences. 
For now this is a prototype in Python, sketching out the concept until it perhaps finds a more suitable way to exist.
Below is a bit of description of the structure so far and the ideas.

Still work in progress. It's prototyping the idea before migrating it something more useful with GUI and all.

## Usage
run main.py 
edit the file TestInstructions.txt for now to create sequences and tracks.

### Operators on sequences and tracks
For now part can be either a sequence or euclidean sequence. That can created by doing for example A = [1,0,0,0] for a sequence or B = (5,6) for a euclidean sequence. 
Tracks are created with {} brackets. 
To combine the parts assign them to a track with a note value and operatros. 
for example t1 = {36, A|B}
This will create a track that triggers note 36 and is a combination of A or B. 
Operators to use for now are & and, | or, ^ xor. 


## Code concepts:
Below is an overview of the conceps in the code.

### Part
A part is either a euclidean sequnece or manual entered sequence of any length. 
Its a list of 1's and 0's. 1 means trigger, 0 means don't do anything


### Track
A track holds an instruction set of which parts should be combined and in what order. They hold a note as well which is the one triggered when a Instruction set returns 1 from the parts. 
A track doesn't hold a length, it will just querry a part at the position the sequence is in. All Parts loop wrap around themselves. 

This way if a part is 6 triggers long and one is 8, the Sequencer position being at 7 will querry the first part at position 0 in the list, and at 7 in the second one. 
This can create interesting pattern variations and polythimcal feels. 


### Sequence
is the beat that runs all the Tracks. Tracks are added to the sequence.
