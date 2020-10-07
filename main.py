from ev3dev2.display import Display
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2._platform.ev3 import INPUT_2
from ev3dev2.sound import Sound
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D, SpeedPercent



def int2color(colornr):
    if colornr == 0:
        print("NoColor")
        s.speak('This is not a color')
    elif colornr == 1:
        print("Black")
        s.speak('Black')
    elif colornr == 2:
        print("Blue")
        s.speak('Blue')
    elif colornr == 3:
        print("Green")
        s.speak('Green')
    elif colornr == 4:
        print("Yellow")
        s.speak('Yellow')
    elif colornr == 5:
        print("Red")
        s.speak('Red')
    elif colornr == 6:
        print("White")
        s.speak('White')
    elif colornr == 7:
        print("Brown")
        s.speak('Brown')
    else:
        print("No valid value") 
        s.speak('Value not valid')

s = Sound()


my_display = Display()
#ts = TouchSensor(INPUT_1)
cs = ColorSensor(INPUT_2)
new_color = 0 
prev_color = 0
my_display.clear()
print("test color sensor")
while True:
    new_color = cs.color
    if new_color != prev_color:
        prev_color = new_color
        int2color(new_color)
