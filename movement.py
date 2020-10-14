from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D, SpeedRPS, SpeedPercent, LargeMotor
from time import sleep

class movement:
    def canMoveForward(self):
        return not (self.v.onBorder() or self.v.isColliding() or self.v.isCloseToColliding())
    
    def forward(self, rotations):    
        self.engine.on_for_rotations(self.speedPerc, self.speedPerc, rotations, brake=True, block=False)    
              
        while self.canMoveForward() and self.engine.is_running :
            sleep(self.sensorInterval)
            
        self.engine.off(brake=True)
        if not self.canMoveForward():
            self.u.mSpeak('Blocked!')
            
            
    '''
    Tries to move backward, but does not guarantee that the robot stays within operational parameters.
    '''
    def backward(self, rotations):
        self.engine.on_for_rotations(self.negSpeedPerc, self.negSpeedPerc, rotations, block=True)
            
    '''
    use direction = 0 to do nothing, direction = -1 for left (counterclockwise) and direction = 1 for right (clockwise)
    '''
    def rotate(self, direction, rotations):       
        if direction < 0: 
            print('left')
            self.engine.on_for_rotations(self.negSpeedPerc, self.speedPerc, rotations, block=False)
            while (not self.u.checkTouchR()) and self.engine.is_running :
                sleep(self.sensorInterval)
        elif direction > 0:
            print('right')
            self.engine.on_for_rotations(self.speedPerc, self.negSpeedPerc, rotations, block=False)
            while (not self.u.checkTouchL()) and self.engine.is_running :
                sleep(self.sensorInterval)
                
        self.engine.off(brake=True)
                
        if self.u.checkTouchR() or self.u.checkTouchL():
            self.u.mSpeak('Could not rotate, collision!')
    
    
    def __init__(self, vitals, utils):
        self.v = vitals
        self.u = utils
        
        speed = 50
        self.speedPerc = SpeedPercent(speed) 
        self.negSpeedPerc = SpeedPercent(-speed) 
        self.sensorInterval = 0.005
        
        self.engine = MoveTank(OUTPUT_A, OUTPUT_D)
        self.left_motor = LargeMotor(OUTPUT_A)