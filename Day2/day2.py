input_file = "input.txt"

input_data = []

with open(input_file, 'r') as file:
        input_data = file.readlines()[0].strip()

input_data = input_data.split(',')

ranges = [(int(r[0]), int(r[1])) for r in (x.split('-') for x in input_data)]

sum = 0

for r in ranges:
    for n in range(r[0], r[1]+1):
        if len(str(n)) % 2 == 0:
            first_half = str(n)[:len(str(n))//2]
            second_half = str(n)[len(str(n))//2:]
            if first_half == second_half:
                sum += n
                
print(f"The sum of all invalid IDs is {sum}")