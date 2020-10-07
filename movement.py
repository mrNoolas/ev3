from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D, SpeedRPS, SpeedPercent

class movement:
    def canMoveForward(self):
        return not (self.v.onBorder() or self.v.isColliding())
    
    def forward(self, rotations):
        while self.canMoveForward() and rotations > 0:
            self.engine.on_for_rotations(self.speedPerc, self.speedPerc, 0.01)
            rotations -= 0.01
            
        if not self.canMoveForward():
            self.u.mSpeak('Blocked by something, cannot move forward!')
            
            
    '''
    Tries to move backward, but does not guarantee that the robot stays within operational parameters.
    '''
    def backward(self, rotations):
        self.engine.on_for_rotations(self.negSpeedPerc, self.negSpeedPerc, rotations)
            
    '''
    use direction = 0 to do nothing, direction = -1 for left (counterclockwise) and direction = 1 for right (clockwise)
    '''
    def rotate(self, direction, rotations):
        if direction < 0:
            while (not self.u.touchR) and rotations > 0:
                self.engine.on_for_rotations(self.speedPerc, self.negSpeedPerc, 1)
                rotations -= 1
        elif direction > 0:
            while (not self.u.touchL) and rotations > 0:
                self.engine.on_for_rotations(self.negSpeedPerc, self.speedPerc, 1)
                rotations -= 1
                
        if self.u.touchR or self.u.touchL:
            self.u.mSpeak('Could not complete rotation due to collision!')
    
    
    def __init__(self, vitals, utils):
        self.v = vitals
        self.u = utils
        
        self.speedPerc = SpeedPercent(20) 
        self.negSpeedPerc = SpeedPercent(-20) 
        
        self.engine = MoveTank(OUTPUT_A, OUTPUT_D)