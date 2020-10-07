from ev3dev2.sound import Sound
from ev3dev2.display import Display

class utils:
    def int2color(self, colornr):
        if colornr == 0:
            print("NoColor")
            self.s.speak('This is not a color')
        elif colornr == 1:
            print("Black")
            self.s.speak('Black')
        elif colornr == 2:
            print("Blue")
            self.s.speak('Blue')
        elif colornr == 3:
            print("Green")
            self.s.speak('Green')
        elif colornr == 4:
            print("Yellow")
            self.s.speak('Yellow')
        elif colornr == 5:
            print("Red")
            self.s.speak('Red')
        elif colornr == 6:
            print("White")
            self.s.speak('White')
        elif colornr == 7:
            print("Brown")
            self.s.speak('Brown')
        else:
            print("No valid value") 
            self.s.speak('Value not valid')
            
    def __init__(self):
        self.s = Sound()
        self.display = Display()
        
        self.display.clear()