import itertools
from typing import List, Tuple

input_file = "input.txt"
def read_data(input_file):
    input_data = []

    with open(input_file, 'r') as file:
        data = file.readlines()
    # Note we cast each line to a list of characters so we can access individual positions
        input_data = [list(line.strip()) for line in data]
    return input_data

input_data = read_data(input_file)

# print(input_data)


def get_neighborhood(grid: List, row: int, col: int) -> List:
    nrow, ncol = len(grid), len(grid[0])
    idx_min_row, idx_max_row = max(0, row - 1), min(nrow, row + 2)
    idx_min_col, idx_max_col = max(0, col - 1), min(ncol, col + 2)
    
    return [grid[r][c] for r in range(idx_min_row, idx_max_row) for c in range(idx_min_col, idx_max_col) if (r, c) != (row, col)]

# Part 1 - How many positions are accessible?

def get_num_accessible(grid: List, debug: bool = False) -> Tuple[int, List]:
    nrow, ncol = len(grid), len(grid[0])

    good = 0

    for row, col in itertools.product(range(nrow), range(ncol)):
        if debug:
            print(f"Checking position {row},{col} ({grid[row][col]})")

        if grid[row][col] == "@":
            tiles = get_neighborhood(grid, row, col)
            n_rolls = sum(t in ["@", "O"] for t in tiles)
            if debug:
                print(f"{tiles=} - {n_rolls=}")
            if n_rolls < 4:
                good += 1
                grid[row][col] = "O" # Mark as accessible

    return (good, grid)

test_input = ["..@@.@@@@.",
              "@@@.@.@.@@",
              "@@@@@.@.@@",
              "@.@@@@..@.",
              "@@.@@@@.@@",
              ".@@@@@@@.@",
              ".@.@.@.@@@",
              "@.@@@.@@@@",
              ".@@@@@@@@.",
              "@.@.@@@.@."]
test_input = [list(line) for line in test_input]

#assert(get_num_accessible(test_input)[0] == 13)
accessible = get_num_accessible(input_data)
print(f"There are {accessible[0]} positions that are accessible")

# Part 2 - Iteratively remove accessible rolls 

input_data = read_data(input_file)

total_accessible = 0

while True:
    n_accessible, input_data = get_num_accessible(input_data)
    # Remove all accessible rolls
    for row, col in itertools.product(range(len(input_data)), range(len(input_data[0]))):
        if input_data[row][col] == "O":
            input_data[row][col] = "."
            total_accessible += 1
    
    # print(f"Accessible positions this iteration: {n_accessible}")
    if n_accessible == 0:
        break

print(f"Total accessible positions after iterative removal: {total_accessible}")