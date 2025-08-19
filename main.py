import random
from robot import Robot

#GLOBLE LIST TO STORE ROBOT's USED IDS
ASSIGNED_ROBOT_IDS = [] 
#GLOBLE LIST TO STORE ROBOT's USED NAMES
ASSIGNED_ROBOT_NAMES = [] 


#expand_direction -> robot class
#greeting -> robot class
#navigating -> robot class


def get_robot_id(number_of_robots):
    """ Create a unique ID for each robots.

    Args:
        number_of_robots(int): current active robots
    Returns:
        int: a unique robot id 
    """
    id_list = []
    
    for i in range(1,number_of_robots+3):
        id = 1000 + i
        id_list.append(id)
    
    while True:
        robot_id = random.choice(id_list)
        if robot_id not in ASSIGNED_ROBOT_IDS:
            ASSIGNED_ROBOT_IDS.append(robot_id)
            return robot_id
    

def get_robot_name():
    """Select a random unused robot name from a text file.
    
    Returns:
        str: a unique robot name
    """
    names = []
    
    #textfile = open("robot_names.txt")
    with open("robot_names.txt") as textfile:
        for name in textfile:
            robot_name = name.strip()
            names.append(robot_name)
    
    while True:
        name = random.choice(names)
        if name not in ASSIGNED_ROBOT_NAMES:
            ASSIGNED_ROBOT_NAMES.append(name)
            return name


def setup_robot(grid_size,number_of_robots):
    """Initialise the robot name, ID and initial direction, postion.
    
    Args:
        grid_size(int): the size of the grid
        number_of_robots(int): numbers of active robots

    Returns:
        Robot: an initialized Robot object with name, ID, position, and direction
    """ 
    
    robot_name = get_robot_name()
    robot_id = get_robot_id(number_of_robots)
    #RANDOM row and column 
    robot_row_index = random.randrange(grid_size)
    robot_col_index = random.randrange(grid_size)
    position = (robot_row_index, robot_col_index)
    #robot_initial_direction = input("Enter starting direction (n/s/e/w):")         #Input direction
    direction = ["w", "s", "n", "e"]
    robot_initial_direction = random.choice(direction)
    
    return Robot(robot_id, robot_name, position, robot_initial_direction)




def run_simulation(grid_size = 10, target_row=9, target_col=9, number_of_robots = 3 ):
    """Start robot navigation simulation
    
    Args:
        grid_size(int): the size of the grid. Default = 10
        target_row(int): currently unused. Placeholder for a single destination row. Default = 9
        target_col(int): currently unused. Placeholder for a single destination column.. Default = 9
        number_of_robots (int): the number of robots to simulate. Default is 3
    """    
    
    targets = [(0,9),(9,9),(9,0),(0,0)]
    robot_list = []
    
    for _ in range(number_of_robots):
        robot_list.append(setup_robot(grid_size,number_of_robots))

    for robot in robot_list:
        robot.robot_greeting()

    
    for i in range(len(robot_list)):
        current_target_row, current_target_col = targets[i] 
        robot_list[i].navigating(current_target_row, current_target_col, grid_size)
    
    
grid_size = 10
number_of_robots = 4
run_simulation(grid_size=grid_size,number_of_robots=4)



    
