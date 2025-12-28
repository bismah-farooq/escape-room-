import door_factory
import basic_door
import random
import locked_door
import combo_door

class EasyDoorFactory(door_factory.DoorFactory):
    def create_door(self):
        easy_door = random.choice([basic_door.BasicDoor(), locked_door.LockedDoor(), combo_door.ComboDoor()])
        return easy_door
    
        
