# The Wonderful Robot 
**Why I created this project?**

This project is started as a way for me to learn and also as an exercise:
* Python OOP (using class and method) 
* Refactoring skills (turning functions into class method) 
* Git & Github workflows (branching, merging,commits and also pushing code to remote repo) 

This project is a simple simulation of robots navigating inside a grid (n x n grid)
Each robot has:
* A unique ID and name
* Staring postion and target position (row, column)
* Direction its facing toward (north, south, east, west)

### How to use  

**1. Clone the repo**
```bash
git clone <HTTP/SSH>
cd robot
```

**2. Run the simulation**
```bash
python3 main.py
```

**3. Custom the robots**

Edit parameters inside ```main.py```
    * grid_size : side of the board
    * number_of_robots : how many robots to simulate
    * target: each robot’s destination (modify inside run_simulation function)

# What the robot will do

* Each robot introduces itself with its name and ID.
* It starts at a random position with a random facing direction.
* It tries to reach its assigned target cell on the grid.
* If it encounters a wall, it turns 90° clockwise and keeps moving.
* Once it reaches the target, it prints a success message.

Example output:
```bash
# number of robot is 4
# target destination = [(0,9),(9,9),(9,0),(0,0)]
# Each robot will have random unique names and get name inside robot_names.txt
# Each robot will have random ID unique generated inside get_robot_id function

Hello, my name is M.A.L.I.C.E.. My ID is 1003
Hello, my name is Alpha-01. My ID is 1001
Hello, my name is HK-47. My ID is 1004
Hello, my name is R-420. My ID is 1006

NAME: M.A.L.I.C.E. |ID: 1003 is navigating
Starting navigation...
My current cordinate is ([7, 3]). Im facing North
My current cordinate is ([6, 3]). Im facing North
My current cordinate is ([5, 3]). Im facing North
My current cordinate is ([4, 3]). Im facing North
My current cordinate is ([3, 3]). Im facing North
My current cordinate is ([2, 3]). Im facing North
My current cordinate is ([1, 3]). Im facing North
My current cordinate is ([0, 3]). Im facing North
I have a wall in front of me!
Turning 90 degrees clockwise
My current cordinate is ([0, 3]). Im facing East
My current cordinate is ([0, 4]). Im facing East
My current cordinate is ([0, 5]). Im facing East
My current cordinate is ([0, 6]). Im facing East
My current cordinate is ([0, 7]). Im facing East
My current cordinate is ([0, 8]). Im facing East
Arrived at target destination (0, 9)

NAME: Alpha-01 |ID: 1001 is navigating
Starting navigation...
My current cordinate is ([0, 0]). Im facing East
My current cordinate is ([0, 1]). Im facing East
My current cordinate is ([0, 2]). Im facing East
My current cordinate is ([0, 3]). Im facing East
My current cordinate is ([0, 4]). Im facing East
My current cordinate is ([0, 5]). Im facing East
My current cordinate is ([0, 6]). Im facing East
My current cordinate is ([0, 7]). Im facing East
My current cordinate is ([0, 8]). Im facing East
My current cordinate is ([0, 9]). Im facing East
I have a wall in front of me!
Turning 90 degrees clockwise
My current cordinate is ([0, 9]). Im facing South
My current cordinate is ([1, 9]). Im facing South
My current cordinate is ([2, 9]). Im facing South
My current cordinate is ([3, 9]). Im facing South
My current cordinate is ([4, 9]). Im facing South
My current cordinate is ([5, 9]). Im facing South
My current cordinate is ([6, 9]). Im facing South
My current cordinate is ([7, 9]). Im facing South
My current cordinate is ([8, 9]). Im facing South
Arrived at target destination (9, 9)

NAME: HK-47 |ID: 1004 is navigating
Starting navigation...
My current cordinate is ([3, 7]). Im facing East
My current cordinate is ([3, 8]). Im facing East
My current cordinate is ([3, 9]). Im facing East
I have a wall in front of me!
Turning 90 degrees clockwise
My current cordinate is ([3, 9]). Im facing South
My current cordinate is ([4, 9]). Im facing South
My current cordinate is ([5, 9]). Im facing South
My current cordinate is ([6, 9]). Im facing South
My current cordinate is ([7, 9]). Im facing South
My current cordinate is ([8, 9]). Im facing South
My current cordinate is ([9, 9]). Im facing South
I have a wall in front of me!
Turning 90 degrees clockwise
My current cordinate is ([9, 9]). Im facing West
My current cordinate is ([9, 8]). Im facing West
My current cordinate is ([9, 7]). Im facing West
My current cordinate is ([9, 6]). Im facing West
My current cordinate is ([9, 5]). Im facing West
My current cordinate is ([9, 4]). Im facing West
My current cordinate is ([9, 3]). Im facing West
My current cordinate is ([9, 2]). Im facing West
My current cordinate is ([9, 1]). Im facing West
Arrived at target destination (9, 0)

NAME: R-420 |ID: 1006 is navigating
Starting navigation...
My current cordinate is ([0, 2]). Im facing West
My current cordinate is ([0, 1]). Im facing West
Arrived at target destination (0, 0)
```

# Future Improvements
This project is still evolving. Some possible improvements include:
* Pathfinding Algorithms: Instead of just turning clockwise when hitting a wall, the robot could use algorithms like BFS (Breadth-First Search), DFS, or A* to find the shortest path.
* Visualization: Replace text output with a graphical interface so users can watch the robots move.
* AI Behavior : I still don't have any idea on how to implement AI into my robot. But this is a cool idea so I keep it here to remind me later 
