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
    initial_input = input("Welcome!")
    robot_name = get_robot_name()
    robot_id = 1000
    #RANDOM row and column 
    robot_row_index = random.randrange(grid_size)
    robot_col_index = random.randrange(grid_size)
    robot_initial_direction = input("Enter starting direction (n/s/e/w):")         #Input direction

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
             grid_size):

    """Move the robot toward the target until it arrives.

    Args: 
        robot_initial_direction(str): the direction robot is facing
        robot_row_index(int): robot's current row coordinate
        robot_col_index(int): robot's current column coordinate
        targer_row(int): the destination's row coordinate
        targer_col(int): the destination's column coordinate
        grid_size(int): grid size of the board (9x9)
    
    """
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
                robot_initial_direction = "e"      #new direction
                
    print(f"Arrived at target destination ({target_row},{target_col})")


def run_simulation(grid_size = 10, target_row=9, target_col=9 ):
    """Start robot navigate simulation
    
    Args:
        grid_size(int): The size of the grid. Default = 10
        target_row(int): The destination row. Default = 9
        target_col(int): The destination column. Default = 9
    """    
    name, id, row, col, direction = setup_robot(grid_size)
    robot_greeting(name, id)
    navigate(direction, row, col, target_row, target_col, grid_size)


grid_size = 10
run_simulation(grid_size=grid_size)

    
