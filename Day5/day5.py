from typing import List

input_file = "input.txt"

ranges = []
ingredients = []
newline_found = False

with open(input_file, 'r') as file:
    data = file.readlines()
    for line in data:
        if line.strip() == "":
            newline_found = True
            continue

        if not newline_found:
            ranges.append(line.strip().split('-'))
        else:
            ingredients.append(int(line.strip()))

for item in ranges:
    item[0] = int(item[0])
    item[1] = int(item[1])

# Part 1 - Find the number of fresh ingredients


def get_fresh_ingredients(ranges: List, ingredients: List) -> int:
    fresh_ingredients = 0

    for ingredient in ingredients:
        fresh = any(r[0] <= ingredient <= r[1] for r in ranges)
        if fresh:
            fresh_ingredients += 1

    return fresh_ingredients


test_ranges = [[3, 5],
               [10, 14],
               [16, 20],
               [12, 18]]

test_ingredients = [1, 5, 8, 11, 17, 32]

assert (get_fresh_ingredients(test_ranges, test_ingredients) == 3)

fresh_ingredients = get_fresh_ingredients(ranges, ingredients)

print(f"The number of fresh ingredients is {fresh_ingredients}")

# Part 2 - Find the number of all possible fresh ingredients


def merge_ranges(ranges: List) -> List:
    # Sort ranges by their start value
    ranges = sorted(ranges, key=lambda x: x[0])

    # Check for overlapping ranges and merge them
    merged = []
    cur_start, cur_end = ranges[0]

    for s, e in ranges[1:]:
        if s <= cur_end:                  # overlapping e.g [1,5] and [4,8]
            cur_end = max(cur_end, e)     # extend e.g to [1,8]
        else:
            # no overlap, add the previous range
            merged.append([cur_start, cur_end])
            cur_start, cur_end = s, e     # continue with the new range

    merged.append([cur_start, cur_end])

    return merged

def get_all_fresh_ingredients(ranges: List) -> int:
    merged_ranges = merge_ranges(ranges)
    return sum((r[1] - r[0] + 1) for r in merged_ranges)

assert(merge_ranges([[1, 3], [2, 4], [15, 27], [13, 25]]) == [[1, 4], [13, 27]])
assert(merge_ranges([[5, 10], [1, 4], [8, 12]]) == [[1, 4], [5, 12]])

assert(get_all_fresh_ingredients(test_ranges) == 14)

all_fresh = get_all_fresh_ingredients(ranges)
print(f"The number of all possible fresh ingredients is {all_fresh}")
