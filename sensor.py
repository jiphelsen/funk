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
            parent["axion"].act(parent["setter"],output)
        return output
    
    def reset(self):
        self.__cooldown = 0

    def add_parent(self,parent,setter):
        self.parents.append({"axion":parent,"setter":setter})
    
    def wait(self):
        if self.__cooldown ==0:return
        self.__cooldown-=1