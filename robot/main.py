import random

#GLOBLE LIST TO STORE ROBOT's USED IDS
assigned_robot_ids = []
#GLOBLE LIST TO STORE ROBOT's USED NAMES
assigned_robot_names = []

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

def get_robot_id(number_of_robots):
    id_list = []
    
    for i in range(1,number_of_robots+3):
        id = 1000 + i
        id_list.append(id)
    
    while True:
        robot_id = random.choice(id_list)
        if robot_id not in assigned_robot_ids:
            assigned_robot_ids.append(robot_id)
            return robot_id
    

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
    
    while True:
        name = random.choice(names)
        if name not in assigned_robot_names:
            assigned_robot_names.append(name)
            return name


def setup_robot(grid_size,number_of_robots):
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

    robot = {}
    robot_name = get_robot_name()
    robot_id = get_robot_id(number_of_robots)
    #RANDOM row and column 
    robot_row_index = random.randrange(grid_size)
    robot_col_index = random.randrange(grid_size)
    position = (robot_row_index, robot_col_index)
    #robot_initial_direction = input("Enter starting direction (n/s/e/w):")         #Input direction
    direction = ["w", "s", "n", "e"]
    robot_initial_direction = random.choice(direction)
    
    robot["id"] = robot_id
    robot["name"] = robot_name
    robot["position"] = position
    robot["direction"] = robot_initial_direction
    
    return robot

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
        robot_initial_direction(str): the direction robot is facing
        robot_row_index(int): robot's current row coordinate
        robot_col_index(int): robot's current column coordinate
        targer_row(int): the destination's row coordinate
        targer_col(int): the destination's column coordinate
        grid_size(int): grid size of the board (9x9)
    
    """
    target_postition = (target_row,target_col)
    current_postion = list(robot["position"])
    
    print()
    print(f"NAME: {robot["name"]} |ID: {robot["id"]} is navigating")
    print("Starting navigation...")
    
    #LOGIC for direction 
    while tuple(current_postion) != target_postition:
        print(f"My current cordinate is ({current_postion}). Im facing {expand_direction(robot["direction"])}")
       
        #Hit North
        if robot["direction"] == "n":
            if current_postion[0] > 0:
                print("Move one step forward")
                current_postion[0] = current_postion[0] - 1
            else: 
                print("I have a wall in front of me!")
                print("Turning 90 degrees clockwise ")
                robot["direction"] = "e"      #new direction
                           
        #Hit West
        elif robot["direction"] == "w":
            if current_postion[1] > 0:
                print("Move one step forward")
                current_postion[1] = current_postion[1] - 1          
            else: 
                print("I have a wall in front of me!")
                print("Turning 90 degrees clockwise ")
                robot["direction"] = "n"      #new direction
                    
        #Hit East
        elif robot["direction"] == "e":
            if current_postion[1] < grid_size - 1:
                    print("Move one step forward")
                    current_postion[1] = current_postion[1] + 1
            else: 
                    print("I have a wall in front of me!")
                    print("Turning 90 degrees clockwise ")
                    robot["direction"] = "s"      #new direction
                    
        #Hit South
        elif robot["direction"] == "s":
            if current_postion[0] < grid_size - 1:
                print("Move one step forward")
                current_postion[0] = current_postion[0] + 1 
            else: 
                print("I have a wall in front of me!")
                print("Turning 90 degrees clockwise ")
                robot["direction"] = "w"      #new direction
                
    print(f"Arrived at target destination ({target_postition})")


def run_simulation(grid_size = 10, target_row=9, target_col=9, number_of_robots = 3 ):
    """Start robot navigate simulation
    
    Args:
        grid_size(int): The size of the grid. Default = 10
        target_row(int): The destination row. Default = 9
        target_col(int): The destination column. Default = 9
    """    
    
    targets = [(0,0),(0,9),(9,9)]
    robot_list = []
    
    for _ in range(number_of_robots):
        robot_list.append(setup_robot(grid_size,number_of_robots))

    for i in range(number_of_robots):
        robot_greeting(robot_list[i]["name"], robot_list[i]["id"])

    for i in range(number_of_robots):
        current_target_row = targets[i][0]
        current_target_col = targets[i][1]
        navigate(robot_list[i], current_target_row,current_target_col, grid_size,)
        
    
grid_size = 10

run_simulation(grid_size=grid_size,number_of_robots=3)




    
