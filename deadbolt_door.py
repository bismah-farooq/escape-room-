import door
import random

class DeadBoltDoor(door.Door):
    def __init__(self):
        self._bolt1 = random.randint(0, 1) #0 means unlocked, 1 means locked
        self._bolt2 = random.randint(0, 1)

    def examine_door(self):
        return "a double deadbolt door. Both need to be unlocked to open the door, but you can't tell by looking at them if they're locked or unlocked."

    def menu_options(self):
        return "1. Toggle Bolt 1\n2. Toggle Bolt 2\n"
    
    def get_menu_max(self):
        return 2

    def attempt(self, option): 
        if option == 1:
            if self._bolt1 == 0:
                self._bolt1 = 1
            else:
                self._bolt1 = 0

            return "You toggle the first bolt."
        else:
            if self._bolt2 == 0:
                self._bolt2 = 1
            else:
                self._bolt2 = 0

            return "You toggle the second bolt."
        
    def is_unlocked(self):
        return self._bolt1 == 0 and self._bolt2 == 0

    def clue(self):
        if (self._bolt1 == 0 and self._bolt2 == 1) or (self._bolt1 == 1 and self._bolt2 == 0):
            return "You jiggle the door.. it seems like one of the bolts is unlocked."
        
        if self._bolt1 == 1 and self._bolt2 == 1:
            return "You jiggle the door... it seems like its completely locked."

    def success(self):
        return "You unlocked both deadbolts and unlocked the door."