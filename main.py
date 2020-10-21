from utils import utils
from vitals import vitals
from checkColor import checkColor
from movement import movement
from threading import Thread
from doMovements import doMovements
from time import sleep



def main():
    u = utils()
    v = vitals(u)
    m = movement(v, u) 
    
    move = doMovements(v,m)
    c = checkColor(u)
#     a = py(v,m)
#     s = checkColor(v, m)
        
#    while True:       
#        # random rotation in direction
#        rot = random.randint(-6, 6) / 10
#        print(rot)
#        #m.rotate(rot, abs(rot))
#        m.safeRotate(rot, abs(rot))
#        
#        # random forward unless collision
#        dr = random.randint(5, 20) / 10
#        m.forward(dr)
#        
#        # backward if collision
#        if v.isColliding() or v.onBorder():
#            m.backward(0.2)

        
#     behaviors = [move,a,s]
    behaviors = [move,c]    
    print("Start thread 1")
    Thread(target=go, args=[behaviors]).start()
    print("Start thread 2")
    Thread(target=doAction, args=[behaviors]).start()

    
def go(behaviors):
    activeBehavior = 0 #Standard = movement
    highest = 0 #Standard = movement
    behaviors[highest].active = True
    while not behaviors[1].foundAllColors: 
        #print("Current running behavior " + str(activeBehavior))
        print("Colors to be checked:")
        print(behaviors[1].colorsToFind)
        for i in range(len(behaviors)-1, -1, -1):
            if i > activeBehavior:
                if behaviors[i].takeControl() and behaviors[activeBehavior].active:
                    print("Behavior " + str(i) + " wants to take control!")
                    print("Suppressing behavior " + str(activeBehavior))
                    behaviors[activeBehavior].suppress()
                    print("Starting behavior " + str(i))
                    behaviors[i].suppressed = False
                    behaviors[i].active = True
                    activeBehavior = i
            elif not behaviors[activeBehavior].active:
                #No behavior is running, thus the highest can be started. 
                if behaviors[i].takeControl():
                    print("Starting behavior " + str(i))
                    behaviors[i].suppressed = False
                    behaviors[i].active = True
                    activeBehavior = i        
        sleep(0.5)
            
def doAction(behaviors):
    while not behaviors[1].foundAllColors:
        for i in range(len(behaviors)-1, -1, -1): 
            if behaviors[i].active:
                #print("Thread 2 runs behavior " + str(i))
                behaviors[i].action();
    
main()
