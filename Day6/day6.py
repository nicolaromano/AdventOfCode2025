import numpy as np

input_file = "input.txt"

values = []
with open(input_file, 'r') as file:
    data = file.readlines()

    for line in data[:-1]:
        values.append([int(x) for x in line.strip().split()])

    operations = data[-1].strip().split()

# Part 1 - Calculate the final result based on operations    
# OK, maybe numpy is overkill for this, but it makes the code cleaner
values = np.array(values)
colsums = np.sum(values, axis=0)
colproducts = np.prod(values, axis=0)

result = sum(colsums[i] if operations[i] == "+" else colproducts[i] for i in range(len(operations)))

print(f"Part 1 - The final result is {result}")

# Part 2 - Now alignment matters so need to read the data differently

values = []
with open(input_file, 'r') as file:
    data = file.readlines()

    # Split into single characters
    for line in data[:-1]:
        values.append(list(line.strip()))
        
    operations = data[-1].strip().split()

test_data = [['1', '2', '3', ' ', '3', '2', '8', ' ', ' ', '5', '1', ' ', '6', '4', ' '],
             [' ', '4', '5', ' ', '6', '4', ' ', ' ', '3', '8', '7', ' ', '2', '3', ' '],
             [' ', ' ', '6', ' ', '9', '8', ' ', ' ', '2', '1', '5', ' ', '3', '1', '4']]
test_operations = ['*', '+', '*', '+']

def process_values(values: list) -> np.ndarray:
    arr = np.array(values)
    arr = np.transpose(arr)
    arr = arr[::-1]  # Reverse the rows to have the least significant digit at the bottom
    
    return arr

def get_result(values:np.ndarray, operations:list) -> int:
    int_values = []
    sums = []
    products = []
    
    operations = operations[::-1]  # Reverse operations to match the order of processed values

    for v in values:
        # Groups of numbers are separated by rows of spaces
        # so we check if there is any non-space character in the column (a number is present)
        if any(c != ' ' for c in v):
            int_values.append(int(''.join(v)))
        else:
            sums.append(sum(int_values))
            products.append(np.prod(int_values))
            int_values = [] # Reset for next group
            
    # Handle the last group
    if int_values:
        sums.append(sum(int_values))
        products.append(np.prod(int_values))
                
    return sum(sums[i] if operations[i] == "+" else products[i] for i in range(len(operations)))
            
test_data = process_values(test_data)
assert(get_result(test_data, test_operations) == 3263827)

values = process_values(values)
res = get_result(values, operations)
print(f"Part 2 - The final result is {res}")