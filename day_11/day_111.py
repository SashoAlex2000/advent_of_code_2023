from itertools import combinations

import os
import sys
from typing import Union

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(root_dir)

from utils.python_utils import file_reader, get_file_name_input_file

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

real_input = file_reader(get_file_name_input_file())

def distance_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance


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
    meta_shred.insert(indx + r_incrementer, new_row)
    r_incrementer += 1
    # row_indexes_no_galaxies.pop(0)
    # row_indexes_no_galaxies = [x + 1 for x in row_indexes_no_galaxies]

print('----------------------------------')

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

for indx in cols_no_galaxies:
    print(cols_no_galaxies)
    for row in meta_shred:
        row.insert(indx + incrementer, '.')
    print(f"Inserted at index: {indx + incrementer}")
    incrementer += 1

print('----------------------------------')

for r in meta_shred:
    print(r)

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

for point_1, point_2 in coords_pairs:
    current_distance = distance_between_points(point1=point_1, point2=point_2)
    total_distance += current_distance

print(f"Total distance is: {total_distance}")
