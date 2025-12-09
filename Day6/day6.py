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

print(f"The final result is {result}")

