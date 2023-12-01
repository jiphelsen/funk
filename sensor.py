import type_utils
class Sensor:
    def __init__(self,input_function,input_speed,name):
        self.input_function = input_function
        self.input_speed = input_speed
        self.__cooldown = 0
        self.name = name
        self.parents = []

    def percept(self,world):
        if self.__cooldown !=0: 
            self.__cooldown-=1
            return None
        self.__cooldown = self.input_speed
        output = self.input_function(world)
        for parent in self.parents:
            parent.update(output)
        return output
    
    def add_parent(self,parent):
        self.parents.append(parent)