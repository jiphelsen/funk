import copy
from sensor import Sensor
class simulation:
    def __init__(self,world):
        self.world = copy.deepcopy(world)
        self.bu_world = copy.deepcopy(world)
        self.__sensors = []

    def print_world(self):
        print(self.world)
    
    def reset_world(self):
        self.world = copy.deepcopy(self.bu_world)

    def add_sensor(self,input_function,input_speed,name):
        self.__sensors.append(Sensor(input_function,input_speed,name))

    def get_sensors(self):
        return copy.deepcopy(self.__sensors)
    
    def run(self,duration):
        for tick in range(0,duration):
            print("hey")
            


