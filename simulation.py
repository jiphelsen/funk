from sensor import Sensor




# 1 represents dirty 0 represent clean
real_world = {"world_map":[1,0],"position":1}
def print_world_state():
    print(real_world)

camera_input =  lambda input_world : input_world["world_map"][input_world["position"]]
camera = Sensor(camera_input,1,"camera")

for tick in range(0,10):
    #print_world_state()
    if tick == 5: real_world["position"] = 0
    print(camera.percept(real_world))

