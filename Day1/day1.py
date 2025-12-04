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

