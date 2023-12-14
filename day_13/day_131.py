import os
import sys
from typing import Union

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(root_dir)

from utils.python_utils import file_reader, get_file_name_input_file

test_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

my_file = open('input_13.txt')

real_input = my_file.read()

my_file.close()

# test_test = test_input.split('\n\n')
test_test = real_input.split('\n\n')
print(len(test_test))
meta_shred: list[list[list[str]]] = []

# tt is each input to be checked
for tt in test_test:
    splitt = tt.split('\n')  # get individual line
    cur = []
    for ss in splitt:
        if ss.strip() == '':
            continue
        second_split = list(ss)
        cur.append(second_split)

    [print(x) for x in cur]
    print('---------------------')
    meta_shred.append(cur)


vertical_found: list[int] = []
horizontal_rows_found: list[int] = []


for reflection_map in meta_shred:
    magic_integer = -1
    print(f"Len reflection map: {len(reflection_map[0])}")
    for i in range(0, len(reflection_map[0]) - 1):
        print(f"Checking i: {i}")
        inner_reflection_bool = True
        left = i
        right = i + 1
        while left >= 0 and right < len(reflection_map[0]):
            for row in reflection_map:
                # print(f"row: {row}")
                if row[left] != row[right]:
                    # print(f"Difference found: {row[left]} is not equal to {row[right]}")
                    inner_reflection_bool = False
                    break
            if inner_reflection_bool is False:
                
                break
            left -= 1
            right += 1

        if inner_reflection_bool:
            magic_integer = i + 1
            break
            
    if magic_integer > 0:
        vertical_found.append(magic_integer)
        print(f"Magic vertical index?: {magic_integer}")
        continue
    
    
    # search rows
    for r in range(0, len(reflection_map)):
        left_row = r
        right_row = r + 1
        row_mirror = True

        while left_row >= 0 and right_row < len(reflection_map):
            print(f"left row: {left_row}; right row: {right_row}; len: {len(reflection_map)}")
            print(f"{reflection_map[0]}")
            current_left_row = reflection_map[left_row]
            current_right_row = reflection_map[right_row]
            for c in range(len(current_left_row)):
                if current_left_row[c] != current_right_row[c]:
                    row_mirror = False
                    break
            if row_mirror is False:
                break

            left_row -= 1
            right_row += 1
        
        if row_mirror is True:
            print(f"Found a horizontal match @: {r}")
            magic_integer = r + 1
            horizontal_rows_found.append(magic_integer)
            break

    

total_score = 0

for v in vertical_found:
    total_score += v

for h in horizontal_rows_found:
    total_score += 100 * h

print(f"Final score is: {total_score}")
    
