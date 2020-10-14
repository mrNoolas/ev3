

class stayInBorder:
    def takeControl(self):
        return self.v.onBorder()
        
    def action(self):
        self.active = True
        if not self.suppress:
            self.movement.backward()
        self.active = False
    
    def suppress(self):
        self.suppress = True
        
    def __init__(self, vitals, movement, priority):
        self.v = vitals
        self.movement = movement
        self.priority = priority
        self.active = False

        