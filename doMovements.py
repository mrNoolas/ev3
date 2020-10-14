import random

class doMovements:
    def takeControl(self):
        return True
    
    def action(self):
        print("test color sensor")
        print(self.suppressed)
        print(self.active)
        while (not self.suppressed) and self.active:       
            # random rotation in direction
            rot = random.randint(-6, 6) / 10
            print(rot)
            self.m.rotate(rot, abs(rot))
            
            # random forward unless collision
            dr = random.randint(5, 20) / 10
            print("Moving forward")
            self.m.forward(dr)
        self.active = False
        
    def suppress(self):
        self.suppressed = True
    
    
    def __init__(self, vitals, movement):
        self.v = vitals
        self.m = movement
        
        self.suppressed = False
        self.active = False