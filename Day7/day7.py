from functools import cache

input_file = "input.txt"

with open(input_file, 'r') as file:
    values = file.readlines()

test_data = [".......S.......",
"...............",
".......^.......",
"...............",
"......^.^......",
"...............",
".....^.^.^.....",
"...............",
"....^.^...^....",
"...............",
"...^.^...^.^...",
"...............",
"..^...^.....^..",
"...............",
".^.^.^.^.^...^.",
"..............."]

# Part 1 - Count the number of splits - each splitter (^) splits the beam into two beams
def count_splits(input:list[str]) -> int:
    # We save beam positions as a set of tuples (col, row)
    # This way, if two splitters split the beam to the same position, we only count it once
    beam_pos = {(input[0].find("S"), 0)}
    num_splits = 0

    for row in range(1, len(input)):
        for col, val in enumerate(input[row]):
            if val == ".":
                for beam in list(beam_pos):
                    if beam[1] == row-1 and beam[0] == col:
                        beam_pos.add((col, row))
            elif val == "^":
                if (col, row-1) in beam_pos:
                    # We add two new beam positions left and right of the splitter
                    beam_pos.add((col-1, row))
                    beam_pos.add((col+1, row))
                    num_splits += 1
    
    return num_splits

assert(count_splits(test_data) == 21)

print(f"Part 1 - The number of splits is {count_splits(values)}")

# Part 2 - Splitters randomly move the beams left or right, so we need to track all possible beam positions
# This is essentially a DFS through the grid

@cache # Memoization to avoid recalculating paths from the same position
# Note: we pass input as a tuple because lists are not hashable, and we can't @cache them
def count_paths(input:tuple[str], beam_pos_x:int, beam_pos_y:int) -> int:
    if beam_pos_y >= len(input) -1:
        return 1
    
    if input[beam_pos_y][beam_pos_x] == ".": # Empty space, beam continues straight
        return count_paths(input, beam_pos_x, beam_pos_y+1)
    elif input[beam_pos_y][beam_pos_x] == "^": # Splitter, beam splits left and right
        return (count_paths(input, beam_pos_x-1, beam_pos_y+1) +
                count_paths(input, beam_pos_x+1, beam_pos_y+1))
    else: # Invalid position (outside the grid)
        return 0
    
bpx, bpy = test_data[0].find("S"), 0
assert(count_paths(tuple(test_data[1:]), bpx, bpy) == 40)

bpx, bpy = values[0].find('S'), 0
print(f"Part 2 - The number of possible paths is {count_paths(tuple(values[1:]), bpx, bpy)}")