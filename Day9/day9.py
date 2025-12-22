import numpy as np

input_file = "input.txt"

input_data = []
with open(input_file, 'r') as file:
    lines = file.readlines()
    input_data.extend([int(x) for x in l.strip().split(',')] for l in lines)

test_data = np.array([
[7,1],
[11,1],
[11,7],
[9,7],
[9,5],
[2,5],
[2,3],
[7,3]])

def get_max_area(data:np.ndarray) -> int:
    max_area = 0
    for p1 in data[:-1]:
        for p2 in data[1:]:
            if np.array_equal(p1, p2) or p1[0] == p2[0] or p1[1] == p2[1]:
                continue
            # Note the (annoying!) +1, because of how areas are defined!
            
            area = (abs(p2[0]-p1[0])+1) * (abs(p2[1]-p1[1])+1)
            max_area = max(max_area, area)
            
    return max_area

assert(get_max_area(test_data) == 50)

print(get_max_area(input_data))