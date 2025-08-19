class Robot:
    """Represents a robot with unique ID, name, position, and facing direction.
    
    Attributes:
        id (int): Unique identifier for the robot.
        name (str): Robot's name.
        position (tuple[int, int]): (row, column) position on the grid.
        direction (str): Direction the robot is facing ("North", "South", "East", "West").
    """
    def __init__(self, identifier, name, position, direction):
        self.id = identifier
        self.name = name
        self.position = list(position)
        self.direction = direction

    def expand_direction(self, short):
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
    
    
    def robot_greeting(self):
        """ Printing what robot "say"
        
        Args:
            name(str): robot's name
            id(int): robot's id
        """
        print(f"Hello, my name is {self.name}. My ID is {self.id}")


    def move_forward(self,grid_size):
        """Try to move robot 1 step forward in its current direction
        
        Args:
            grid_size(int): size of the grids
        """
        if self.direction == "n" and self.position[0] > 0:
            self.position[0] -= 1
        elif self.direction == "e" and self.position[1] < grid_size - 1:
            self.position[1] += 1
        elif self.direction == "s" and self.position[0] < grid_size -1:
            self.position[0] +=1
        elif self.direction == "w" and self.position[1] > 0:
            self.position[1] -=1
        else:
            print("I have a wall in front of me!")


    def turn_clockwise(self):
        """Turn robot 90 degrees clock wise 
        when hit the wall and face it new direction"""
        
        direction = ["n", "e", "s", "w"]
        current_index = direction.index(self.direction)
        self.direction = direction[(current_index+1) % 4]


    def navigating(self, target_row, target_col, grid_size):
        """Move the robot toward the target until it arrives.

        Args: 
            robot (Robot): the robot object containing its current position, direction, and ID.
            target_row (int): the destination's row coordinate.
            target_col (int): the destination's column coordinate.
            grid_size (int): the size of the square grid
        """
        target_postition = (target_row, target_col)
        print()
        print(f"NAME: {self.name} |ID: {self.id} is navigating")
        print("Starting navigation...")

        while tuple(self.position) != target_postition:
            print(f"My current cordinate is ({self.position}). Im facing {self.expand_direction(self.direction)}")

            before_position = tuple(self.position)
            self.move_forward(grid_size)

            if tuple(self.position) == before_position:
                print("Turning 90 degrees clockwise")
                self.turn_clockwise()
        
        print(f"Arrived at target destination {target_postition}")


if __name__ == "__main__" :
    grid_size = 10
    target_row = 9
    target_col = 0
    robot = Robot(1234, "Elon Musk", (1,2), "n")
    robot.robot_greeting()
    robot.navigating(target_row=target_row,
                     target_col=target_col,
                     grid_size=grid_size)

        