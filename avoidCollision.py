
class avoidCollision:
    def takeControl(self):
        return self.v.isColliding() or self.v.isCloseToColliding()
        
    def action(self):
        if not self.suppress:
            self.movement.backward()
    
    def suppress(self):
        self.suppress = True
        
    def __init__(self, vitals, movement, priority):
        self.v = vitals
        self.movement = movement
        
        self.priority = priority
        self.suppress = False
        self.active = False