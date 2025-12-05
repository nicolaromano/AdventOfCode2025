input_file = "input.txt"

input_data = []

with open(input_file, 'r') as file:
        input_data = file.readlines()[0].strip()

input_data = input_data.split(',')

ranges = [(int(r[0]), int(r[1])) for r in (x.split('-') for x in input_data)]

# Part 1 - Sum of all invalid IDs made by repeating the same digits twice

def check_invalid_id(n:int) -> bool:
    '''
    Check if the number n is made by repeating the same digits twice
    
    Parameters:
    n (int): The number to check
    
    Returns:
    bool: is n invalid ID?
    '''
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

# Part 2 - Invalid IDs made by repeating the same digits a number of times

def check_invalid_id_2(n:int) -> bool:
    n_str = str(n)
    length = len(n_str)
    for size in range(1, length//2 + 1):
        if length % size == 0: # size must divide length
            times = length // size
            if n_str[:size] * times == n_str:
                return True
    return False

sum = 0

for r in ranges:
    for n in range(r[0], r[1]+1):
        if check_invalid_id_2(n):
            sum += n
                
print(f"The sum of all invalid IDs (pt 2) is {sum}")
