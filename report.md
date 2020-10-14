# DES assignment 6,  Gerhard van der Knijff s1006946, David Vonk s4681533

## Notes 

We divided our solution over multiple files, to create maximal generalization.
Our program is started from the main.py file. This file contains a while loop which 
makes the robot rotate randomly and move forward (if possible). If the robot cannot move forward,
the robot moves backward.

We also have a utils.py file. In this file are the functions to register the values of the different
sensors. These functions can be called in the other files if needed. 

The next file we have is a vitals.py file. This file contains functions to check if the robot
is on the border, is colliding or is close to an object. These functions ask for the values of the
sensors in utils.py.

The last file we have is movement.py. This file handles all the movements of the robot. There 
are functions to rotate, move forward and move backward. 

In the next exercises, we can extend the utils, the vitals and the movements easily if necessary.

### Observations:
If we set the speed of the robot to high, the robot will fall off the map, because the color
sensor cannot handle the color fast enough to stop the rotation. A solution would be to 
interrupt the rotations if the color sensor registers black.  