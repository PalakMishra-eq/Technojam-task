# Technojam-task_6
Complexity of a garland:
First thing that we need to understand is that the complexity of the garland is defined by number of pairs, of adjacent toys, which have different parity ie different remainder when divided by 2.
For example, the complexity of 1 4 2 3 5 is 2
1&4 have remainders 1&0 res,
4&2 have remainders 0&0 res,
2&3 have remainders 0&1 res,
3&5 have remainders 1&1 res.
So we have two pairs with different parity ie 2&3 and 1&4, hence complexity is 2.

When we create a program for the above problem we start with taking a variable for number of toys removed, then creating a matrix for storing and comparing the complexities of the adjacent pairs of toys,
zero is the removed toy so it is not taken into consideration.


# Technojam-task_7
Validating an email using regex and tkinter:
First thing, create a tkinter window for desktop, a simple screen login screen.
Then import the built-in package re for using RegEx module. 
Declare variable for storing password and then creating function for validation of email.
Also a driver code for getting email and calling validation function.


# Technojam-task_8
LOOK disc-scheduling algorithm:
LOOK is the advanced version of SCAN (elevator) disk scheduling algorithm which gives slightly better seek time than any other algorithm in the hierarchy (FCFS->SRTF->SCAN->C-SCAN->LOOK).
Let Request array represents an array storing indexes of tracks that have been requested in ascending order of their time of arrival. ‘head’ is the position of disk head.
The initial direction in which head is moving is given and it services in the same direction.
The head services all the requests one by one in the direction head is moving.
The head continues to move in the same direction until all the request in this direction are not finished.
While moving in this direction calculate the absolute distance of the track from the head.
Increment the total seek count with this distance.
Currently serviced track position now becomes the new head position.
Go to step 5 until we reach at last request in this direction.
If we reach where no requests are needed to be serviced in this direction reverse the direction and go to step 3 until all tracks in request array have not been serviced.
