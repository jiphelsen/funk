class :
    def __init__(self,world,evolution_function):
        self.world = world
        self.evolve = evolution_function
    def update(self,new_data):
        self.world.update(new_data)