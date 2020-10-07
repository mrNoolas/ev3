from utils import utils

class vitals:           
    def onBorder(self):
        isBlack = self.u.checkColor() == 1
        if isBlack :
            self.u.mSpeak('Caution, robot is on border!')
        
        return isBlack
    
    def isColliding(self):
        isColliding = self.u.checkTouchL() or self.u.checkTouchR()
        if isColliding :
            self.u.mSpeak('Collision in the front. Abort Abort!')
            self.u.mBeep()
            self.u.mBeep()
        return isColliding
    
    def isCloseToColliding(self):
        distance = self.u.checkDistance()
        if distance < 180:
            self.u.mSpeak('Collision threat in the front!')
            return True
        return False
        
                
    def __init__(self, utils):
        # Hello!  
        self.u = utils