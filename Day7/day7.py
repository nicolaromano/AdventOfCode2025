input_file = "input.txt"

with open(input_file, 'r') as file:
    values = file.readlines()

print(values)

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

