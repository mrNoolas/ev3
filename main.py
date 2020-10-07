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
        rot = random.randint(-5, 5) / 10
        print(rot)
        m.rotate(rot, abs(rot))
        
        # random forward unless collision
        dr = random.randint(0, 5) / 10
        m.forward(dr)
        
        # backward if collision
        if v.isColliding() or v.onBorder():
            m.backward(0.5)
        
            
main()
