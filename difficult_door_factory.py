import door_factory
import random
import combo_door
import deadbolt_door
import code_door 


class DifficultDoorFactory(door_factory.DoorFactory):
    def create_door(self):
        difficult_door = random.choice([combo_door.ComboDoor(), deadbolt_door.DeadBoltDoor(), code_door.CodeDoor()])
        return difficult_door
    