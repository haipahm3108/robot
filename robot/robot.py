class Robot:
    """Represents a robot with unique ID, name, position, and facing direction.
    
    Attributes:
        id (int): Unique identifier for the robot.
        name (str): Robot's name.
        position (tuple[int, int]): (row, column) position on the grid.
        direction (str): Direction the robot is facing ("n", "s", "e", "w").
    """
    def __init__(self, identifier, name, position, direction):
        self.id = identifier
        self.name = name
        self.position = position
        self.direction = direction



if __name__ == "__main__" :
    robot = Robot(1234, "Elon Musk", (1,2), "North")
    print(robot.name)
    print(robot.id)
    print(robot.position)
    print(robot.direction)

        