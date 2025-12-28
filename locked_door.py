import door
import random

class LockedDoor(door.Door):
    def __init__(self):
        self._solution = random.randint(1, 3)
        self._input = 0

    def examine_door(self):
        return "a locked door. Look around you, the key is hidden nearby."

    def menu_options(self):
        return "1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock\n"

    def get_menu_max(self):
        return 3

    def attempt(self, option):
        self._input = option

        if self._input == 1:
            return "You look under the door mat."
        if self._input == 2:
            return "You look under the flower pot."
        else:
            return "You look under the fake rock."
        
    def is_unlocked(self):
        return self._input == self._solution

    def clue(self):
        return "Look somewhere else."

    def success(self):
        return "Congratulations, you opened the door."