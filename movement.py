from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D, SpeedRPS, SpeedPercent, LargeMotor
import random

class movement:
    def takeControl(self):
        return True
    
    def action(self):
        self.active = True
        while not self.suppress:       
            # random rotation in direction
            rot = random.randint(-5, 5) / 10
            print(rot)
            self.rotate(rot, abs(rot))
            
            # random forward unless collision
            dr = random.randint(0, 5) / 10
            self.forward(dr)
        self.active = False
        
    def suppress(self):
        self.suppres = True
    
    def canMoveForward(self):
        return not (self.v.onBorder() or self.v.isColliding() or self.v.isCloseToColliding())
    
    def forward(self, rotations):       
        while self.canMoveForward() and rotations > 0:
            if self.u.checkDistance() > 300 and self.u.checkDistance() < 2500:
                self.engine.on_for_rotations(self.speedPerc, self.speedPerc, self.movementQuantum, brake=False)
            else:
                self.engine.on_for_rotations(self.speedPerc, self.speedPerc, self.smallMovementQuantum, brake=False)
                rotations -= self.smallMovementQuantum          
            
        self.engine.off(brake=True)
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
    
    
    def __init__(self, vitals, utils, priority):
        self.v = vitals
        self.u = utils
        
        self.speedPerc = SpeedPercent(100) 
        self.negSpeedPerc = SpeedPercent(-100) 
        self.movementQuantum = 0.1
        self.smallMovementQuantum = 0.02
        
        self.engine = MoveTank(OUTPUT_A, OUTPUT_D)
        self.left_motor = LargeMotor(OUTPUT_A)
        
        self.priority = priority
        self.active = False
        self.suppress = False