import door
import random

class BasicDoor(door.Door):
    def __init__(self):
        self._solution = random.randint(1, 2)
        self._input = 0

    def examine_door(self):
        return "a basic door. You can either push or pull it to open."

    def menu_options(self):
        return "1. Push\n2. Pull\n"

    def get_menu_max(self):
        return 2

    def attempt(self, option):
        self._input = option

        if self._input == 1:
            return "You push the door."
        else:
            return "You pull the door."
        
    def is_unlocked(self):
        return self._input == self._solution

    def clue(self):
        return "Try the other way."

    def success(self):
        return "Congratulations, you opened the basic door."