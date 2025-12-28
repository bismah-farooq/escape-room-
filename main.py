import check_input
import easy_door_factory
import difficult_door_factory

def open_door(door):
    print("\nYou encounter " + door.examine_door())

    while door.is_unlocked() == False:
        print(door.menu_options())

        user_choice = check_input.get_int_range("Enter choice: ", 1, door.get_menu_max())

        print()
        print(door.attempt(user_choice))
        
        if door.is_unlocked():
            print()
            print(door.success())
        else:
            print()
            print(door.clue())

def main():
    print("\nWelcome to the escape room.\nYou must unlock 3 doors to escape...")
    difficulty = check_input.get_int_range("Enter difficulty (1. Easy 2. Hard): ", 1, 2)
    doors_opened = 0

    if difficulty == 1: 
        factory = easy_door_factory.EasyDoorFactory()
    else:
        factory = difficult_door_factory.DifficultDoorFactory()
        
    while doors_opened != 3:
        encounter = factory.create_door()

        open_door(encounter)
        doors_opened += 1

    print("\nCongratulations! You escaped... this time.")

main()