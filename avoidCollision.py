
class avoidCollision:
    def takeControl(self):
        return self.v.isColliding() or self.v.isCloseToColliding()
        
    def action(self):
        if self.active and not self.suppressed:
            self.m.backward(0.2)
        self.active = False
    
    def suppress(self):
        self.suppressed = True
        
    def __init__(self, vitals, movement):
        self.v = vitals
        self.m = movement

        self.suppressed = False
        self.active = False