from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D, SpeedRPS, SpeedPercent, LargeMotor

class movement:
    def canMoveForward(self):
        return not (self.v.onBorder() or self.v.isColliding())
    
    def forward(self, rotations):
        while self.canMoveForward() and rotations > 0:
            self.engine.on_for_rotations(self.speedPerc, self.speedPerc, self.movementQuantum)
            rotations -= self.movementQuantum
            
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
            print('left')
            while (not self.u.checkTouchR()) and rotations > 0:
                self.engine.on_for_rotations(self.negSpeedPerc, self.speedPerc, self.movementQuantum)
                rotations -= self.movementQuantum
        elif direction > 0:
            print('right')
            while (not self.u.checkTouchL()) and rotations > 0:
                self.engine.on_for_rotations(self.speedPerc, self.negSpeedPerc, self.movementQuantum)
                
                rotations -= self.movementQuantum
                
        if self.u.checkTouchR() or self.u.checkTouchL():
            self.u.mSpeak('Could not complete rotation due to collision!')
    
    
    def __init__(self, vitals, utils):
        self.v = vitals
        self.u = utils
        
        self.speedPerc = SpeedPercent(100) 
        self.negSpeedPerc = SpeedPercent(-100) 
        self.movementQuantum = 0.05
        
        self.engine = MoveTank(OUTPUT_A, OUTPUT_D)
        self.left_motor = LargeMotor(OUTPUT_A)