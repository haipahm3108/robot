
"""
##2D -> 1D
user_rows = int(input("Enter row number: "))
user_cols = int(input("Enter col numbers: "))
row_index = int(input("Enter row index: "))
col_index = int(input("Enter col index: "))

index_1D = user_cols * row_index + col_index

print(f"The 1D is {index_1D}")
"""
"""
#1D -> 2D
user_rows = int(input("Enter row number: "))
user_cols = int(input("Enter col numbers: "))
user_index = int(input("Enter index number: "))

row_index = user_index // user_cols
col_index = user_index % user_cols

print(f"vector is ({row_index},{col_index})")
"""
#3D -> 1D
"""
d1 = int(input("Enter dimenstion 1: "))
d2 = int(input("Enter dimenstion 2: "))
d3 = int(input("Enter dimenstion 3: "))
index_d1 = int(input("Enter the index of dimentions 1: "))
index_d2 = int(input("Enter the index of dimentions 2: "))
index_d3 = int(input("Enter the index of dimentions 3: "))

flatten_index =  index_d1 * d2 * d3 + index_d2 * d3 + index_d3

print(f"the index is {flatten_index}")
"""
"""
#index -> 3D 
d1 = int(input("Enter dimenstion 1: "))
d2 = int(input("Enter dimenstion 2: "))
d3 = int(input("Enter dimenstion 3: "))
index = int(input("Index: "))

index_d1 = index // (d2*d3)
remaining = index % (d2*d3)
index_d2 = remaining // d3
index_d3 = remaining % d3

print(index_d1)
print(index_d2)
print(index_d3)

# r1 = ('SV02', 'Trần Ngọc Minh', 'Nữ', Null, 'CNP2020')
# r2 = ('SV01', 'Nguyễn Văn An', 'Nam', 'TPHCM', 'CNP2020')
"""
# leap year check
"""
year = int(input("Enter a year: "))

if year % 4 == 0:
    if(year % 100 == 0):
        if (year % 400 == 0):
            print("is leap year")
        else:
            print("is not leap year")
    else:
        print("is leap year")
else:
    print("not leap year")
"""


# thermostat program
"""
user_temperature = float(input("Enter temperature: "))

if user_temperature > 22:
    print("to hot")
    user_temperature -= 1
    print(f"new temperature {user_temperature}")
elif user_temperature < 20:
    print("too cold")
    user_temperature += 1
    print(f"new temperature {user_temperature}")
else:
    print("Just nice!")
    print(f"new temperature {user_temperature}")
"""
#CONST
robot_id = 1000

#USER input
robot_name = input("Enter robot name: ")
robot_row_index = int(input("Enter robot row index: "))
robot_col_index = int(input("Enter robot col index: "))
robot_initial_direction = input("What is its initial direction [n|s|e|w]? ")

#NEW LOGIC FOR (row,col)
robot_row_index = max(0,min(robot_row_index,9))
robot_col_index = max(0,min(robot_col_index,9))

#OLD LOGIC FOR (row,col)
"""
if robot_row_index < 0:
    robot_row_index = 0
if robot_row_index > 9:
    robot_row_index = 9
"""
postion = "my postion"

if robot_col_index <= 4:
    if robot_row_index <= 4:
        postion = "top left quadrant"
    else:
        postion = "bottom left quadrant"
else:
    if robot_row_index <= 4:
        postion = "top right quadrant"
    else:
        postion = "bottom right quadrant"

print(f"My name cordinate is ({robot_row_index},{robot_col_index}). My postion is: {postion}")
print(f"My name is {robot_name} and my ID: {robot_id}")
print("update")

#LOGIC for direction 
if robot_initial_direction == "n":
    robot_row_index = robot_row_index - 1
    if robot_row_index < 0:
        robot_row_index = 0
    if robot_row_index < 5:
        if robot_col_index < 5:
            postion = "top lef quadrant"
        else:
            postion = "top right qudrant"
    print("Im facing North")

elif robot_initial_direction == "w":
    robot_col_index = robot_col_index - 1
    if robot_col_index < 0:
        robot_col_index = 0
    if robot_col_index < 5:
        if robot_row_index < 5:
            postion = "top left quadrant"
        else:
            postion = "bottom left qudrant"
    print("Im facing West")    

elif robot_initial_direction == "e":
    robot_col_index = robot_col_index +1
    if robot_col_index > 9:
        robot_col_index = 9
    if robot_col_index > 4:
        if robot_row_index > 4:
            postion = "bottom right quadrant"
        else:
            postion = "top right quadrant"
    print("Im facing East")

elif robot_initial_direction == "s":
    robot_row_index = robot_row_index +1
    if robot_row_index > 9:
        robot_row_index = 9
    if robot_row_index > 4:
        if robot_col_index > 4:
            postion = "bottom right quadrant"
        else:
            postion = " bottom left quadrant"
    print("Im facing South")

print(f"My current cordinate is ({robot_row_index},{robot_col_index}). My postion is: {postion}")

    