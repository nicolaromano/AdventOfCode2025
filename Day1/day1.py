def rotate_dial(start: int, direction: str, steps: int, total_steps: int = 99) -> int:
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


# Test cases for rotate_dial (start, direction, steps, expected)
test_cases = [(0, "R", 10, 10),
              (10, "L", 5, 5),
              (50, "L", 68, 82),
              (99, "R", 1, 0),
              (52, "R", 48, 0)
              ]

for case in test_cases:
    result = rotate_dial(case[0], case[1], case[2])
    assert (
        result == case[3]), f"Test failed for input {case}. Expected {case[3]}, got {result}"

input_file = "input.txt"

input_data = []

with open(input_file, 'r') as file:
    data = file.readlines()
    for line in data:
        # Each line is in the format: "<direction><steps>"
        input_data.append((line[0], int(line[1:].strip())))

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


def get_pwd_2(input_data, starting_position, max_steps=99, debug=False):
    password = 0

    for i in input_data:
        direction, steps = i

        if debug:
            print(
                f"Starting Position: {starting_position}, Current Password: {password}")

        if direction == "L":
            # We cross 0 after starting_position steps, then every (max_steps + 1) steps after that
            first_crossing = starting_position if starting_position != 0 else max_steps + 1

            if steps >= first_crossing:
                ncrossings = 1 + (steps - first_crossing) // (max_steps + 1)
                password += ncrossings

        if direction == "R":
            # We cross 0 after (max_steps + 1 - starting_position) steps, then every (max_steps + 1) steps after that
            first_crossing = (max_steps + 1 - starting_position)

            if steps >= first_crossing:
                ncrossings = 1 + (steps - first_crossing) // (max_steps + 1)
                password += ncrossings

        starting_position = rotate_dial(
            starting_position, direction, steps, max_steps)

        if debug:
            print(
                f"After moving {direction} {steps}, new position: {starting_position}, Current Password: {password}\n")

    return password

# Test cases for part 2

test_cases_2 = [[("L", 30),  # 50 -> 20
                 ("R", 10),  # 20 -> 30
                 ("L", 31),  # 30 -> 99 (crosses 0)
                 ("R", 2)    # 99 -> 1 (crosses 0)
                 ],
                
                [("R", 60),  # 50 -> 10 (crosses 0)
                 ("L", 20),  # 10 -> 90 (crosses 0)
                 ("R", 15),  # 90 -> 5 (crosses 0)
                 ("L", 5)    # 5 -> 0 (lands on 0)
                 ],
                
                [("L", 10),  # 50 -> 40
                 ("R", 20),  # 40 -> 60
                 ("L", 15),  # 60 -> 45
                 ("R", 5)    # 45 -> 50
                 ],
                
                [("R", 355)  # 50 -> 5 (crosses 0 four times)
                 ],
                
                [("L", 68),  # 50 -> 82 (crosses 0)
                 ("L", 30),  # 82 -> 52
                 ("R", 48),  # 52 -> 0 (lands on 0)
                 ("L", 5),   # 0 -> 95 
                 ("R", 60),  # 95 -> 56 (crosses 0)
                 ("L", 55),  # 56 -> 1
                 ("L", 1),   # 1 -> 0 (lands on 0)
                 ("L", 99),  # 0 -> 1
                 ("R", 14),  # 1 -> 15
                 ("L", 82)   # 15 -> 33
                 ]]

test_cases_2_results = [2, 4, 0, 4, 6]

for i in range(len(test_cases_2)):
    result = get_pwd_2(test_cases_2[i], 50)
    assert (result == test_cases_2_results[i]), f"Test failed for input {test_cases_2[i]}. Expected {test_cases_2_results[i]}, got {result}"

password2 = get_pwd_2(input_data, 50)

print(f"The password for part 2 is {password2}")
