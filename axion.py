class Axion:
    def __init__(self,init_world,condition_action_map,root_up_map):
        self.world = init_world
        self.reaction_tests
        self.condition_action_map = condition_action_map
        if condition_action_map is None: self.condition_action_map = dict()
        self.root_up_map = root_up_map
        if root_up_map is None : self.root_up_map = dict()

        
    def add_actuator(self,actuator,params,condition):
        self.condition_action_map[condition] ={"actuator" : actuator,"params" : params}

    def act(self,setter,params):
        self.world = setter(self.world,params)
        for condition in self.condition_action_map.keys():
            condition_is_true  = condition(self.world)
            if condition_is_true:
                action = self.condition_action_map[condition]
                action["actuator"](params)



