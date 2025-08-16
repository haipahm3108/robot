import random
from robot import Robot

#GLOBLE LIST TO STORE ROBOT's USED IDS
ASSIGNED_ROBOT_IDS = [] 
#GLOBLE LIST TO STORE ROBOT's USED NAMES
ASSIGNED_ROBOT_NAMES = [] 

def expand_direction(short):
    """Convert a short direction character into its full word.
    
    Args:
        short(str): a single-letter direction
   
     Returns:
         str: the expanded direction ("North", "South", "East", or "West")
    """
    if short == "n":
        return "North"
    elif short == "s":
        return "South"
    elif short == "w":
        return "West"
    elif short == "e":
        return "East"


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


def robot_greeting(name, id):
    """ Printing what robot "say"
    
    Args:
        name(str): robot's name
        id(int): robot's id
    """
    print(f"Hello, my name is {name}. My ID is {id}")


def navigate(robot,
             target_row,
             target_col,
             grid_size,
             ):
    """Move the robot toward the target until it arrives.

    Args: 
        robot (Robot): the robot object containing its current position, direction, and ID.
        target_row (int): the destination's row coordinate.
        target_col (int): the destination's column coordinate.
        grid_size (int): the size of the square grid
    """

    target_postition = (target_row,target_col)
    current_postion = list(robot.position)
    
    print()
    print(f"NAME: {robot.name} |ID: {robot.id} is navigating")
    print("Starting navigation...")
    
    #LOGIC for direction 
    while tuple(current_postion) != target_postition:
        print(f"My current cordinate is ({current_postion}). Im facing {expand_direction(robot.direction)}")
       
        #Hit North
        if robot.direction == "n":
            if current_postion[0] > 0:
                print("Move one step forward")
                current_postion[0] = current_postion[0] - 1
            else: 
                print("I have a wall in front of me!")
                print("Turning 90 degrees clockwise ")
                robot.direction = "e"      #new direction
                           
        #Hit West
        elif robot.direction == "w":
            if current_postion[1] > 0:
                print("Move one step forward")
                current_postion[1] = current_postion[1] - 1          
            else: 
                print("I have a wall in front of me!")
                print("Turning 90 degrees clockwise ")
                robot.direction = "n"      #new direction
                    
        #Hit East
        elif robot.direction == "e":
            if current_postion[1] < grid_size - 1:
                    print("Move one step forward")
                    current_postion[1] = current_postion[1] + 1
            else: 
                    print("I have a wall in front of me!")
                    print("Turning 90 degrees clockwise ")
                    robot.direction = "s"      #new direction
                    
        #Hit South
        elif robot.direction == "s":
            if current_postion[0] < grid_size - 1:
                print("Move one step forward")
                current_postion[0] = current_postion[0] + 1 
            else: 
                print("I have a wall in front of me!")
                print("Turning 90 degrees clockwise ")
                robot.direction = "w"      #new direction
                
    print(f"Arrived at target destination ({target_postition})")


def run_simulation(grid_size = 10, target_row=9, target_col=9, number_of_robots = 3 ):
    """Start robot navigation simulation
    
    Args:
        grid_size(int): the size of the grid. Default = 10
        target_row(int): currently unused. Placeholder for a single destination row. Default = 9
        target_col(int): currently unused. Placeholder for a single destination column.. Default = 9
        number_of_robots (int): the number of robots to simulate. Default is 3
    """    
    
    targets = [(0,0),(0,9),(9,9)]
    robot_list = []
    
    for _ in range(number_of_robots):
        robot_list.append(setup_robot(grid_size,number_of_robots))

    for i in range(number_of_robots):
        robot_greeting(robot_list[i].name, robot_list[i].id)

    for i in range(number_of_robots):
        current_target_row = targets[i][0]
        current_target_col = targets[i][1]
        navigate(robot_list[i], current_target_row,current_target_col, grid_size,)
        
    

grid_size = 10
number_of_robots = 3
run_simulation(grid_size=grid_size,number_of_robots=3)



    
