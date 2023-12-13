from itertools import combinations

import os
import sys
from typing import Union

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(root_dir)

from utils.python_utils import file_reader, get_file_name_input_file

real_input = file_reader(get_file_name_input_file())


test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

my_test_input = """
...#..
......
..#...
......
#.....
"""

MULTIPLIER = 1000000

def manhattan_distance_with_expansion(point1, point2, row_expansion: list, col_expansion: list):
    x1, y1 = point1
    x2, y2 = point2

    min_x = min(x1, x2)
    max_x = max(x1, x2)

    min_y = min(y1, y2)
    max_y = max(y1, y2)

    in_between_rows = [r for r in row_expansion if min_x < r < max_x]
    in_between_cols = [c for c in col_expansion if min_y < c < max_y]

    rows_expanded = len(in_between_rows)  # cannot be equal
    cols_expanded = len(in_between_cols)

    manh_original = abs(x2 - x1) + abs(y2 - y1)
    manh_modified = (abs(x2 - x1) + rows_expanded * (MULTIPLIER - 1)) + (abs(y2 - y1) + cols_expanded * (MULTIPLIER - 1))
    distance = manh_modified # + square_distance    

    return distance


def increment_list_elements_by_thei_index(some_list: list[int]):  # This was creating the bugs !

    for i in range(len(some_list)):
        some_list[i] += i

    
# meta_shred = [[y for y in list(x)] for x in my_test_input.split('\n') if x.strip() != '']
# meta_shred = [[y for y in list(x)] for x in test_input.split('\n') if x.strip() != '']
meta_shred = [[y for y in list(x)] for x in real_input if x.strip() != '']

for r in meta_shred:
    print(r)

# Galaxy expansion
row_indexes_no_galaxies = []
matrix_row_length = len(meta_shred[0])

for indx, row in enumerate(meta_shred):
    flag = any([x for x in row if x != '.'])

    if not flag:
        row_indexes_no_galaxies.append(indx)

# Expand the rows
r_incrementer = 0
for indx in row_indexes_no_galaxies:
    new_row = ['.' for _ in range(matrix_row_length)]



for r in meta_shred:
    print(r)

# expand cols
cols_no_galaxies: list[str] = []

for i in range(matrix_row_length):
    no_galaxies_bool = True
    for row in meta_shred:
        if row[i] != '.':
            no_galaxies_bool = False
            break
    if no_galaxies_bool:
        cols_no_galaxies.append(i)


incrementer = 0
# the value of the traversed list wasnt being updated dynamically?

# ----------------------------------------------------------------------

list_of_coords_tuples: list[tuple[int, int]] = []

for r in range(len(meta_shred)):
    for c in range(len(meta_shred[r])):
        current_symbol = meta_shred[r][c]
        if current_symbol == '#':
            tuple_curr = tuple((r,c))
            list_of_coords_tuples.append(tuple_curr)

print(list_of_coords_tuples)

coords_pairs = list(combinations(list_of_coords_tuples, 2))

print(type(coords_pairs))
print(len(coords_pairs))

print('----------------------------------')

total_distance = 0
row_expansion = 'a'

for point_1, point_2 in coords_pairs:
    
    current_distance = manhattan_distance_with_expansion(point1=point_1, point2=point_2, 
                                                        row_expansion=row_indexes_no_galaxies, 
                                                        col_expansion=cols_no_galaxies)
    print(f"Calculating for points: {point_1}, {point_2}; distance is: {current_distance}")
    total_distance += current_distance

print(f"Total distance is: {total_distance}")
