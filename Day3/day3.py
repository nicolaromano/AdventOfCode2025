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
