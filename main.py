"""The robot can navigate to the end of the board.
"""

import random

def expand_direction(short):
    
    """Handle direction input and turn it into letters
    
    Args:
        short(str): input direction character varible
    Return:
        n -> North
        s -> South
        w -> West
        e -> East
    """
    if short == "n":
        return "North"
    elif short == "s":
        return "South"
    elif short == "w":
        return "West"
    elif short == "e":
        return "East"


def get_robot_name():
    """Get robot name from txt file

    Args:
        robot_name(txt): a file contains all robot names
    
    Return:
        Return the random name get form the txt file
    """
    names = []
    textfile = open("robot_names.txt")
    for name in textfile:
        robot_name = name.strip()
        names.append(robot_name)
    
    index = random.randrange(len(names))
    for i in range(0,len(names)):
        if i == index:
            return names[i]
        
    


def setup_robot(grid_size):
    """Initialise the robot name, ID and intitial direction, postion
    
    Args:
        grid_size(int): The size of the grid

    Return:
        str: Robot name
        int: Robot ID
        int: Robot's row
        int: Robot's column
        str: Robot's direction (n/e/s/w)
    """
    robot_name = get_robot_name()
    robot_id = 1000
    #RANDOM row and column 
    robot_row_index = random.randrange(grid_size)
    robot_col_index = random.randrange(grid_size)
    #robot_initial_direction = input("Enter starting direction (n/s/e/w):")         #Input direction
    direction = ["w", "s", "n", "e"]
    robot_initial_direction = random.choice(direction)
    
    return (robot_name, robot_id, robot_row_index, robot_col_index, robot_initial_direction)

def robot_greeting(name, id):
    """ Printing what robot "say"
    
    Args:
        name(str): robot's name
        id(int): robot's id
    """
    print(f"Hello, my name is {name}. My ID is {id}")


def navigate(robot_initial_direction,
             robot_row_index,
             robot_col_index,
             target_row,
             target_col,
             grid_size,
             name):

    """Move the robot toward the target until it arrives.

    Args: 
        robot_initial_direction(str): the direction robot is facing
        robot_row_index(int): robot's current row coordinate
        robot_col_index(int): robot's current column coordinate
        targer_row(int): the destination's row coordinate
        targer_col(int): the destination's column coordinate
        grid_size(int): grid size of the board (9x9)
    
    """
    print()
    print(f"{name} is navigating")
    print("Starting navigation...")
    #LOGIC for direction 
    while (robot_row_index, robot_col_index) != (target_row,target_col):
        print(f"My current cordinate is ({robot_row_index},{robot_col_index}). Im facing {expand_direction(robot_initial_direction)}")
       
        #Hit North
        if robot_initial_direction == "n":
            if robot_row_index > 0:
                print("Move one step forward")
                robot_row_index = robot_row_index - 1
            else: 
                print("I have a wall in front of me!")
                print("Turning 90 degrees clockwise ")
                robot_initial_direction = "e"      #new direction
                           
        #Hit West
        elif robot_initial_direction == "w":
            if robot_col_index > 0:
                print("Move one step forward")
                robot_col_index = robot_col_index - 1          
            else: 
                print("I have a wall in front of me!")
                print("Turning 90 degrees clockwise ")
                robot_initial_direction = "n"      #new direction
                    
        #Hit East
        elif robot_initial_direction == "e":
            if robot_col_index < grid_size - 1:
                    print("Move one step forward")
                    robot_col_index = robot_col_index + 1
            else: 
                    print("I have a wall in front of me!")
                    print("Turning 90 degrees clockwise ")
                    robot_initial_direction = "s"      #new direction
                    
        #Hit South
        elif robot_initial_direction == "s":
            if robot_row_index < grid_size - 1:
                print("Move one step forward")
                robot_row_index = robot_row_index + 1 
            else: 
                print("I have a wall in front of me!")
                print("Turning 90 degrees clockwise ")
                robot_initial_direction = "w"      #new direction
                
    print(f"Arrived at target destination ({target_row},{target_col})")


def run_simulation(grid_size = 10, target_row=9, target_col=9, number_robots = 3 ):
    """Start robot navigate simulation
    
    Args:
        grid_size(int): The size of the grid. Default = 10
        target_row(int): The destination row. Default = 9
        target_col(int): The destination column. Default = 9
    """    
    targets = [(9,9),(0,9),(9,9)]
    robot_name = []
    robot_rows = []
    robot_cols = []
    robot_direction = []
    for _ in range(number_robots):
        name,id,row,col,direction = setup_robot(grid_size)
        robot_name.append(name) 
        robot_rows.append(row)
        robot_cols.append(col)
        robot_direction.append(direction)

    
    for name in robot_name:
        robot_greeting(name, id)

    for i in range(number_robots):
        current_target_row = targets[i][0]
        current_target_col = targets[i][1]
        navigate(robot_direction[i], robot_rows[i], robot_cols[i], current_target_row, current_target_col, grid_size,robot_name[i])
        
    
grid_size = 10
run_simulation(grid_size=grid_size)

    
