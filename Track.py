from Instruction import Instruction, GetOperation


class Track:
    def __init__(self, note, instructions, parts):
        self._counter = 0
        self._note = note
        self._instructions = instructions
        self._parts = parts

        self.set_instructions()

    def set_instructions(self):
        # build instructions should happen in another place where 
        # when parts added we add them to a dict.
        # when combinations happen we add them as well to the dict so they can be resused. 

        # an instruction set could be a class with bound referneces to the parts in the dict 
        # and then querried from here.
        pass


    def evaluate_next_step(self):
        temp = 0
        for instruction in self.intructionSteps:
            temp = instruction.evaluate_next_step(self._counter)

        self._counter += 1
        return temp
