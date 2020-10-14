from utils import utils
from vitals import vitals
from stayInBorder import stayInBorder
from avoidCollision import avoidCollision
from movement import movement
import threading


def main():
    u = utils()
    v = vitals(u)
    
    m = movement(v, u, 10) 
    a = avoidCollision(v,m, 20)
    s = stayInBorder(v, m , 30)
        
    behaviors = [m,a,s]
    t1 = threading.Thread(target=go)
    t2 = threading.Thread(target=doActions)
    t1.start()
    t2.start()
    
def go():
    
def doAction():
            
main()
