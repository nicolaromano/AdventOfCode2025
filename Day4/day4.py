import itertools
from typing import List

input_file = "input.txt"

input_data = []

with open(input_file, 'r') as file:
    data = file.readlines()
    # Note we cast each line to a list of characters so we can access individual positions
    input_data = [list(line.strip()) for line in data]

# print(input_data)


def get_neighborhood(grid: List, row: int, col: int) -> List:
    nrow, ncol = len(grid), len(grid[0])
    idx_min_row, idx_max_row = max(0, row - 1), min(nrow, row + 2)
    idx_min_col, idx_max_col = max(0, col - 1), min(ncol, col + 2)
    
    return [grid[r][c] for r in range(idx_min_row, idx_max_row) for c in range(idx_min_col, idx_max_col) if (r, c) != (row, col)]


def get_num_accessible(grid: List, debug: bool = False) -> int:
    nrow, ncol = len(grid), len(grid[0])

    good = 0

    for row, col in itertools.product(range(nrow), range(ncol)):
        if debug:
            print(f"Checking position {row},{col} ({grid[row][col]})")

        if grid[row][col] == "@":
            tiles = get_neighborhood(grid, row, col)
            n_rolls = sum(t == "@" for t in tiles)
            if debug:
                print(f"{tiles=} - {n_rolls=}")
            if n_rolls < 4:
                good += 1

    return good

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

assert(get_num_accessible(test_input) == 13)

accessible = get_num_accessible(input_data)
print(f"There are {accessible} positions that are accessible")
