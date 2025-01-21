__WIP__

This is a sequencer that uses sequences generated as euclidean sequences or manually typed, and combines these into poly rythmical sequences. 


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