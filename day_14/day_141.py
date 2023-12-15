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
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

# meta_shred = [[y for y in list(x)] for x in test_input.split('\n') if x.strip() != '']
meta_shred = [[y for y in list(x)] for x in real_input if x.strip() != '']

[print(m) for m in meta_shred]

# new_matrix = [[meta_shred[c] for r in range(len(meta_shred))] for c in range(len(meta_shred[0]))]

new_matrix = []

# TODO -> ONE LINE
for c in range(len(meta_shred[0])):
    curr = []
    for r in range(len(meta_shred)):
        curr.append(meta_shred[r][c])

    new_matrix.append(curr)

print('------------------s')
[print(nm) for nm in new_matrix]


for row in new_matrix:
    print('--------------------')
    print(row)
    round_stones_indexes = []
    first_non_static_rock_index = -1

    for st_index, stone in enumerate(row):

        if stone == '.':
            if first_non_static_rock_index < 0:
                first_non_static_rock_index = st_index

        if stone == 'O':
            round_stones_indexes.append(st_index)
    print(f"Round stone indexes: {round_stones_indexes}")
    print(f"Start is: {first_non_static_rock_index}")
    count_of_stones: int = len(round_stones_indexes)

    for round_stone in round_stones_indexes:

        if round_stone < first_non_static_rock_index:
            continue

        new_index = -1

        for reverse_index in range(round_stone-1, -1, -1):
            if row[reverse_index] == 'O' or row[reverse_index] == '#':
                new_index = reverse_index + 1
                break

            if reverse_index == 0:
                new_index = reverse_index
        # print(f"Round stone with index: {round_stone} has a new place: {new_index}")
        if new_index != round_stone:
            row[new_index] = 'O'
            row[round_stone] = '.'

    print(row)
    print('-------------------------')


[print(r) for r in new_matrix]
total_load_coefficient: int = 0

for reworked_row in new_matrix:
    for indx, re_stone in enumerate(reworked_row):
        if re_stone == 'O':
            total_load_coefficient += (len(reworked_row) - indx)

print(f"The total sum is: {total_load_coefficient}")
