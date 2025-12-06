input_file = "input.txt"

input_data = []

with open(input_file, 'r') as file:
    data = file.readlines()
    for line in data:
        input_data.append(line.strip())

# Part 1 - Calculate the largest joltage from the given string of digits


def get_largest_joltage(num: str) -> int:
    """
    Gets the largest "joltage" from a series of batteries, given you can
    turn on only 2

    Parameters:
    num (str): A string of digits representing battery joltages
    Returns:
    int: The largest possible joltage from turning on 2 batteries. The first number
        represents the tens place, and the second number represents the ones place.
    """
    vals = [int(x) for x in num]
    # Find the largest digit excluding the last
    d1 = max(vals[:-1])
    d1_pos = vals.index(d1)
    # Find the largest digit after the position of d1
    d2 = max(vals[d1_pos+1:])

    return d1 * 10 + d2


# Test cases from prompt
assert (get_largest_joltage("987654321111111") == 98)
assert (get_largest_joltage("811111111111119") == 89)
assert (get_largest_joltage("234234234234278") == 78)
assert (get_largest_joltage("818181911112111") == 92)

total_joltage = sum(get_largest_joltage(v) for v in input_data)

print(f"The total largest joltage is {total_joltage}")

# Part 2 - Now we can turn on 12 batteries

def get_largest_joltage_12(num: str, debug:bool = False) -> str:
    """
    Gets the largest "joltage" from a series of batteries, given you can
    turn on 12

    Parameters:
    num (str): A string of digits representing battery joltages
    Returns:
    int: The largest possible joltage from turning on 12 batteries.
    """

    vals = [int(x) for x in num]
    jottage = ""

    for n in range(12):
        # Find the largest digit excluding the last n
        if debug:
            print(f"Checking max of {vals[:len(vals) - 12 + n + 1]}")

        max_val = max(vals[:len(vals)-12+n+1])
        max_pos = vals.index(max_val)
        jottage += str(max_val)
        vals = vals[max_pos+1:]
        if debug:
            print(f"{n=} {max_val=} {max_pos=} {jottage=}")

    return jottage

assert (get_largest_joltage_12("987654321111111") == "987654321111")
assert (get_largest_joltage_12("811111111111119") == "811111111119")
assert (get_largest_joltage_12("234234234234278") == "434234234278")
assert (get_largest_joltage_12("818181911112111") == "888911112111")

total_joltage_12 = sum(int(get_largest_joltage_12(v)) for v in input_data)
print(f"The total largest joltage from 12 batteries is {total_joltage_12}")
