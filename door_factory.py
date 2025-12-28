import abc 

class DoorFactory:
    @abc.abstractmethod
    def create_door(self):
        pass
