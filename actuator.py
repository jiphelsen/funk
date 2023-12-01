class Actuator:
    def __init__(self,mutator):
        self.mutator = mutator
    def act(self,world,params):
        self.mutator(world,params)

        


