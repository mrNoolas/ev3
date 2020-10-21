
class checkColor:
    def takeControl(self):
        color = self.u.lastColor
        if color != self.lastColor and (color == 2 or color == 4 or color == 5): #Blue, yellow or red  
            self.lastColor = color
            return True
        else: return False 
        
    def action(self):
        if not self.suppressed:
            if self.lastColor in self.colorsToFind:
                self.colorsToFind.remove(self.lastColor)
            self.u.playDebugSound = True
            self.u.mSpeak("Found color!")
            self.u.int2SpeakColor(self.lastColor)
            self.u.playDebugSound = False
            if not self.colorsToFind:
                self.foundAllColors = True
        self.active = False
    
    def suppress(self):
        self.suppressed = True

        
    def __init__(self, utils):
        self.u = utils
        self.lastColor = self.u.lastColor
        
        self.colorsToFind = [2,4,5]
        
        self.foundAllColors = False
        self.active = False
        self.suppressed = False

        