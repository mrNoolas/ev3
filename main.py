from utils import utils
from vitals import vitals
from movement import movement
import random

def main():
    u = utils()
    v = vitals(u)
    m = movement(v, u) 
    
    h = 1.125
    m.safeRotate(1, h)
    
    """
    while True:       
        # random rotation in direction
        rot = random.randint(-6, 6) / 10
        print(rot)
        m.rotate(rot, abs(rot))
        
        # random forward unless collision
        dr = random.randint(5, 20) / 10
        m.forward(dr)
        
        # backward if collision
        if v.isColliding() or v.onBorder():
            m.backward(0.2)
    """
        
            
main()
