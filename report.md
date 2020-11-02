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

### Bluetooth
We used the bluetooth example. This example seems to have some problems with correctly closing the socket. We think this is because it hangs on listening for some message. This could be fixed by sending a close-message which signals the shutdown of the bluetooth-listen thread. The send thread is properly shutting down.

### Staying within the borders
In this version we tried to improve the edge detection. The current rotation algorithm has fairly high reliability. The only known edge case under this new system is corners where the sensor is in such a position that it is on one of the borders, and moves just into the white in the corner, and then back onto the other edge. In this case the robot thinks it is outside of the map, and unsuccesfully attempts to recover.

Another possible improvement is that the robot sometimes goes outside of the border due to some confusion at corners. Generally it knows that it did this, and it manages to recover 9 times out of 10. (i.e. the robot never 'fully' leaves the field, just mostly...)

### Collision avoidance
Anytime a collision is registered with the bumpers of the robot, the robot immediately stops its current movement, and attempts to revert to a known state (e.g. when it is near a border, and might have its sensor outside of the border). The robot also slows down when the distance sensor is measuring a nearby object. In the simulation the bottle is still often swept of the map, but this is not really preventable without doing extensive scanning after every movement. We opted to go for a more easy approach which is good enough in our opinion.

### Finding the colours 
We use a pseudo-random walk to move over the map, inspired by the way some bacteria look for food. This is probably not the most efficient way, but it eventually gets the job done. The advantage of this technique is that it works independent of environment, position and map layout. It is thus a reliable implementation. Furthermore, the assignment did not state that the algorithm had to be efficient...

### Results
The robots get the job done, albeit not very efficiently. The next steps would be to fix the socket closing and to implement a more efficient search sweep.

