from sensor import Sensor
from actuator import Actuator
import copy


# 1 represents dirty 0 represent clean
real_world = {"world_map":[1,0],"position":1}
og_world = copy.deepcopy(real_world)
def print_world_state():
    print(real_world)

def reset_world():
    global real_world
    real_world=og_world

camera_input =  lambda input_world : input_world["world_map"][input_world["position"]]
camera = Sensor(camera_input,1,"camera")


#looks what happens when you do jack shit
for tick in range(0,10):
    #print_world_state()
    percept = camera.percept(real_world)
    if(tick==5):real_world["world_map"][1]=1
    if tick < 6:
        if tick%2==0: assert percept ==0
        else :assert percept is None
    if tick >=6:
        if tick%2==0: assert percept ==1
        else: assert percept is None
    print(percept)
#nothing happens idiot

camera.reset()
reset_world()

def suck(world,pos):
    world["world_map"][pos]=0

sucker = Actuator(suck)

def move(world,direction):
    global real_world
    position = world["position"]
    if direction == "right" and position==1:return
    if direction == "left" and position ==0:return
    world["position"]=1-position

mover = Actuator(move)
    



#you clean boy, you clean good
mono_stable = 0
for tick in range(0,8):
    percept = camera.percept(real_world)
    if(percept==1):
        sucker.act(real_world,real_world["position"])
    elif mono_stable == 1:
        mover.act(real_world,"right")
        mono_stable = 1-mono_stable
        camera.wait()
    else :
        mover.act(real_world,"left")
        mono_stable = 1-mono_stable
        camera.wait()

    print_world_state()
        
    







