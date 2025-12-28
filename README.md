# Escape Room (Factory Method)

This project simulates an escape room game where the player must unlock a series of doors to escape. The program uses the Factory Method design pattern to generate different types of doors based on the selected difficulty level.

## Description
The player must successfully open three doors in order to escape. At the start of the game, the user selects a difficulty level:

- Easy: BasicDoor, LockedDoor, ComboDoor
- Hard: ComboDoor, DeadboltDoor, CodeDoor

Doors are randomly selected using a factory corresponding to the chosen difficulty. Each door type has its own unlocking logic, menu options, and clues.

## Door Types
- BasicDoor: Opened by pushing or pulling
- LockedDoor: Requires searching for a hidden key
- ComboDoor: Opened by entering a number between 1 and 10
- DeadboltDoor: Requires toggling two bolts
- CodeDoor: Requires toggling a three-character code of X and O

## Program Flow
1. The user selects a difficulty level.
2. A factory is created based on the selected difficulty.
3. Three doors are randomly generated using the factory.
4. The user interacts with each door until it is unlocked.
5. After unlocking all three doors, a success message is displayed.

## How to Run
Run the program from the terminal:
```text
python main.py
```
The user is prompted to choose a difficulty and then interact with each door until all are unlocked.

## Learning Objectives
- Implement the Factory Method design pattern
- Practice object-oriented programming in Python
- Use abstract base classes and inheritance
- Handle user input and validation
- Design modular and reusable code

## Notes
- All user input is validated
- Each door instance is randomly initialized
- No global variables are used
- Door logic is fully encapsulated in each class
