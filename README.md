## Overview

### Details
* Name: abdul-v0  

### Description
Mini-Assignment #2: Create a gym environment for 2 functions that intersect at least once, the agent can move along the x-axis in either direction, but doesn’t know where it is. The agent gets a reward when it finds an x coordinate where the functions intersect. The agent only knows the difference of the functions at its location on the x-axis.

### Source
This environment was thought of by Casey Irvine.


## Environment

### Observation
Type: Box(4)

Num | Observation | Min | Max
---|---|---|---
0 | absolute_value(y1 - y2) | -inf | +inf

Note: y1 and y2 are functions of x where they have at least one unique solution to the system of equations. 

### Actions
Type: Box(1)

Num | Action  | Min | Max  
----|--------------|-----|----   
0   | delta x | -5.0| 5.0

Note: delta x is the change in x

### Reward
Reward is 100 when the intersection is reached

### Starting State
absolute_value(y1 - y2) where y1 is a polynomial of degree 2 and y1 is a polynomial of degree 1.

### Episode Termination
1. The intersection of y1 and y2 is reached. 

### Solved Requirements
Considered solved when the intersection of y1 and y2 is reached.