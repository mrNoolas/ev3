from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D, SpeedPercent
from utils import utils
from vitals import vitals
from movement import movement
import random

def main():
    u = utils()
    v = vitals(u)
    m = movement(v, u) 
    
    print("test color sensor")
    while True:       
        # random rotation in direction
        rot = random.randint(-30, 30)
        m.rotate(rot, rot)
        
        # random forward unless collision
        dr = random.randint(0, 2)
        m.forward(dr)
        
        # backward if collision
        if v.isColliding() or v.onBorder():
            m.backward(0.5)
        
            
main()
