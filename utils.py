from ev3dev2.sound import Sound
from ev3dev2.display import Display
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2._platform.ev3 import * 


class utils:
    def int2SpeakColor(self, colornr):
        if colornr == 0:
            print("NoColor")
            self.mSpeak('This is not a color')
        elif colornr == 1:
            print("Black")
            self.mSpeak('Black')
        elif colornr == 2:
            print("Blue")
            self.mSpeak('Blue')
        elif colornr == 3:
            print("Green")
            self.mSpeak('Green')
        elif colornr == 4:
            print("Yellow")
            self.mSpeak('Yellow')
        elif colornr == 5:
            print("Red")
            self.mSpeak('Red')
        elif colornr == 6:
            print("White")
            self.mSpeak('White')
        elif colornr == 7:
            print("Brown")
            self.mSpeak('Brown')
        else:
            print("No valid value") 
            self.mSpeak('Value not valid!')
            
    def checkColor(self):        
        newColor = self.colorSensor.color
        if newColor != self.lastColor:
            self.lastColor = newColor
            self.int2SpeakColor(newColor)
        return self.lastColor
            
    # Moderated speech
    def mSpeak(self, string):
        print(string)
        if self.playDebugSound:
            self.s.speak(string)
            
    def mBeep(self):
        if self.playDebugSound:
            self.s.beep()
            
    def checkTouchL(self):
        touch = self.touchL.is_pressed
        if touch:
            self.mSpeak('The left touch sensor is pressed!')
        return touch  
    
    def checkTouchR(self):
        touch = self.touchR.is_pressed
        if touch:
            self.mSpeak('The right touch sensor is pressed!')
        return touch  
       
            
    def __init__(self):
        self.playDebugSound = False
        self.s = Sound()
        
        self.display = Display()
        self.display.clear()
        
        self.colorSensor = ColorSensor(INPUT_2)
        self.lastColor = 0
        
        self.touchL = TouchSensor(INPUT_1)
        self.touchR = TouchSensor(INPUT_4)
        
        
        
        
        
        
        
        
        
        
        