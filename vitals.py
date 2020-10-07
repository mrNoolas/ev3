from ev3dev2.sensor.lego import ColorSensor
from ev3dev2._platform.ev3 import INPUT_2
import utils    

class vitals:
    def checkColor(self):        
        newColor = self.colorSensor.color
        if newColor != self.lastColor:
            self.lastColor = newColor
            self.utils.int2color(newColor)
    
    def __init__(self, utils):
        # Hello!
        self.colorSensor = ColorSensor(INPUT_2)
        self.lastColor = 0
        self.utils = utils