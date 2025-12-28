import door
import random

class CodeDoor(door.Door):
    def __init__(self):
        self._solution = [random.choice(['X', 'O']), random.choice(['X', 'O']), random.choice(['X', 'O'])]
        self._input = ['X', 'X', 'X']

    def examine_door(self):
        return "a door with a coded keypad with three characters. Each key toggles a value with an ‘X’ or an ‘O’."

    def menu_options(self):
        return "1. Press Key 1\n2. Press Key 2\n3. Press Key 3\n"
    
    def get_menu_max(self):
        return 3

    def attempt(self, option): 
        if option == 1:
            if self._input[0] == 'X':
                self._input[0] = 'O'
            else:
                self._input[0] = 'X'

            return "You toggle the first character."
        elif option == 2:
            if self._input[1] == 'X':
                self._input[1] = 'O'
            else:
                self._input[1] = 'X'

            return "You toggle the second character."
        else:
            if self._input[2] == 'X':
                self._input[2] = 'O'
            else:
                self._input[2] = 'X'

            return "You toggle the third character."
        
    def is_unlocked(self):
        return self._solution == self._input

    def clue(self):
        count = 0
        for i in range(len(self._input)):
            if self._input[i] == self._solution[i]:
                count += 1

        return str(count) + " characters are correct."

    def success(self):
        return "You entered the correct code and opened the door."


