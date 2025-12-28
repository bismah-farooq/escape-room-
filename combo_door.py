import door 
import random

class ComboDoor(door.Door):
    def __init__(self):
        self._solution = random.randint(1, 10)
        self._input = 0

    def examine_door(self):
        return "a door with a combination lock. You can spin the dial to a number 1 - 10."

    def menu_options(self):
        return "Enter a number 1-10:\n"
    
    def get_menu_max(self):
        return 10

    def attempt(self, option):
        self._input = option 
        return f"You turn the dial to... {self._input}"
        
    def is_unlocked(self):
        return self._input == self._solution

    def clue(self):
        if self._input < self._solution:
            return "Too low."
        else:
            return "Too high."

    def success(self):
        return "You found the correct value and opened the door."