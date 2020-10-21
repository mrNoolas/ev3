

class stayInBorder:
    def takeControl(self):
        return self.v.onBorder()
        
    def action(self):
        if not self.suppressed:
            self.movement.backward(0.2)
        self.active = False
    
    def suppress(self):
        self.suppressed = True

        
    def __init__(self, vitals, movement):
        self.v = vitals
        self.movement = movement
        self.active = False
        self.suppressed = False

        