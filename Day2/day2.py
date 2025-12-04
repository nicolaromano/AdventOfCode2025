input_file = "input.txt"

input_data = []

with open(input_file, 'r') as file:
        input_data = file.readlines()[0].strip()

input_data = input_data.split(',')

ranges = [(int(r[0]), int(r[1])) for r in (x.split('-') for x in input_data)]

# Part 1 - Sum of all invalid IDs made by repeating the same digits twice

def check_invalid_id(n:int) -> bool:
    n_str = str(n)
    if len(n_str) % 2 != 0: # odd length can't be invalid
        return False
    half = len(n_str) // 2
    return n_str[:half] == n_str[half:]

sum = 0

for r in ranges:
    for n in range(r[0], r[1]+1):
        if check_invalid_id(n):
            sum += n
                
print(f"The sum of all invalid IDs is {sum}")

# Part 2