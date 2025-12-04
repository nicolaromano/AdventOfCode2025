from pprint import pprint


def rotate_dial(start:int, direction:str, steps:int, total_steps:int = 99) -> int:
    """
    Rotates the dial from a starting position in a given direction by a number of steps.
    
    Parameters:
    start (int): The starting position on the dial (0 to total_steps).
    direction (str): The direction to rotate ('L' for left, 'R' for right).
    steps (int): The number of steps to rotate.
    total_steps (int): The total number of steps on the dial - for this problem it's 99, just included it for generalization.
    """
    
    if (direction not in ['L', 'R']):
        raise ValueError("Direction must be 'L' or 'R'")
    
    if direction == 'L':
        new_position = (start - steps) % (total_steps + 1)
    else:
        new_position = (start + steps) % (total_steps + 1)
        
    return new_position

input_file = "input.txt"

input_data = []

with open(input_file, 'r') as file:
        data = file.readlines()
        for line in data:
            # Each line is in the format: "<direction><steps>"
            input_data.append((line[0], int(line[1:].strip())))

# pprint(input_data)

# Test cases
assert(rotate_dial(0, "R", 10) == 10)
assert(rotate_dial(10, "L", 5) == 5)
assert(rotate_dial(50, "L", 68) == 82)
assert(rotate_dial(99, "R", 1) == 0)
assert(rotate_dial(52, "R", 48) == 0)

starting_position = 50
max_steps = 99
password = 0

# Part 1 - The password is the number of times the dial lands on 0
def get_pwd_1(input_data, starting_position):
    password = 0
    for i in input_data:
        direction, steps = i
        starting_position = rotate_dial(starting_position, direction, steps)
        if starting_position == 0:
            password += 1
            
    return password

password = get_pwd_1(input_data, 50)

print(f"The password for part 1 is {password}")

# Part 2 - The password is the number of times the dial *crosses* 0, even if it doesn't land on it

def get_pwd_2(input_data, starting_position, max_steps=99):
    password = 0    

    for i in input_data:
        direction, steps = i
        
        if direction == "L":
            if (steps >= starting_position): # We're crossing 0 at least once
                ncrossing = (steps - starting_position) // (max_steps + 1) + 1
                password += ncrossing
        else: # direction == "R"
            if (steps > (max_steps - starting_position)):
                ncrossing = (steps - (max_steps - starting_position)) // (max_steps + 1) + 1
                password += ncrossing
            
        starting_position = rotate_dial(starting_position, direction, steps)
    
    return password

# This should give 2 crossings
test_data = [("L", 30), # 50 -> 20
             ("R", 10), # 20 -> 30
             ("L", 31), # 30 -> 99 (crosses 0) 
             ("R", 2)   # 99 -> 1 (crosses 0)
            ]
# This should give 4 crossings
test_data_2 = [("R", 60), # 50 -> 10 (crosses 0)
                ("L", 20), # 10 -> 90 (crosses 0)
                ("R", 15), # 90 -> 5 (crosses 0)
                ("L", 5)   # 5 -> 0 (lands on 0)
               ]

# This should give no crossings
test_data_3 = [("L", 10), # 50 -> 40
                ("R", 20), # 40 -> 60
                ("L", 15), # 60 -> 45
                ("R", 5)   # 45 -> 50
               ]
# This should give 4 crossings
test_data_4 = [("R", 355)] # 50 -> 5 (crosses 0 four times)

test_data_5 = [("L", 68),
               ("L", 30),
                ("R", 48),
                ("L", 5),
                ("R", 60),
                ("L", 55),
                ("L", 1),
                ("L", 99),
                ("R", 14),
                ("L", 82)]

assert(get_pwd_2(test_data, 50) == 2)
assert(get_pwd_2(test_data_2, 50) == 4)
assert(get_pwd_2(test_data_3, 50) == 0)
assert(get_pwd_2(test_data_4, 50) == 4)
assert(get_pwd_2(test_data_5, 50) == 6)

password2 = get_pwd_2(input_data, 50)

print(f"The password for part 2 is {password2}")
