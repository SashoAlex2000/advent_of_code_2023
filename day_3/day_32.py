
import os
import sys
from typing import Union

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(root_dir)

from utils.python_utils import file_reader, get_file_name_input_file

test_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def get_by_index_or_None(some_matrix: list[list[str]], row: int, col: int) -> Union[str, None]:

    if row < 0 or row > len(some_matrix) - 1:
        return None
    
    correct_row = some_matrix[row]

    if col < 0 or col > len(correct_row) - 1:
        return None
    
    return correct_row[col]


def is_element_star(element):

    if element is None:  # important
        return False

    if element == '*':
        return True
    
    return False



def check_if_adjeacent_element_is_star(some_matrix, row, col) -> list[dict[str, int]]:

    adjacent_star_indeces = []

    diagonal_up_left = get_by_index_or_None(some_matrix=some_matrix, row=row-1, col=col-1)
    if is_element_star(diagonal_up_left): adjacent_star_indeces.append({'row': row-1, 'col': col-1})
    
    up = get_by_index_or_None(some_matrix=some_matrix, row=row-1, col=col)
    if is_element_star(up): adjacent_star_indeces.append({'row': row-1, 'col': col})

    diagonal_up_right = get_by_index_or_None(some_matrix=some_matrix, row=row-1, col=col + 1)
    if is_element_star(diagonal_up_right): adjacent_star_indeces.append({'row': row-1, 'col': col + 1})

    left_adjacent = get_by_index_or_None(some_matrix=some_matrix, row=row, col=col - 1)
    if is_element_star(left_adjacent): adjacent_star_indeces.append({'row': row, 'col': col - 1})

    right_adjacent = get_by_index_or_None(some_matrix=some_matrix, row=row, col=col + 1)
    if is_element_star(right_adjacent): adjacent_star_indeces.append({'row': row, 'col': col + 1})

    diagonal_down_right = get_by_index_or_None(some_matrix=some_matrix, row=row+1, col=col - 1)
    if is_element_star(diagonal_down_right): adjacent_star_indeces.append({'row': row+1, 'col': col - 1})

    down = get_by_index_or_None(some_matrix=some_matrix, row=row+1, col=col)
    if is_element_star(down): adjacent_star_indeces.append({'row': row+1, 'col': col})

    diagonal_down_left = get_by_index_or_None(some_matrix=some_matrix, row=row+1, col=col + 1)
    if is_element_star(diagonal_down_left): adjacent_star_indeces.append({'row': row+1, 'col': col + 1})

    return adjacent_star_indeces


# for test input
# lines: list[str] = [x for x in test_input.split('\n') if x.strip() != '']
# matrix = [list(line) for line in lines]

FILE_NAME = get_file_name_input_file()
main_input = file_reader(FILE_NAME)
matrix = [list(line) for line in main_input]

def print_matrix(p_matrix):
    for row in range(len(p_matrix)):
        for col in range(len(p_matrix[row]) - 1):
            print(p_matrix[row][col], end=' ')
        print('\n')


print_matrix(p_matrix=matrix)

total_sum: int = 0

# star_indexes: list[dict[str, Union[int, list[int]]]] = []
star_indeces: dict[int, dict[int, list[int]]] = {

}

"""
{
    0: {
        3: [543]
    },
    3: {
        2: [213, 233]
    }
}
"""

for row in range(len(matrix)):
        
        current_row = matrix[row]

        skip_rows = 0

        for col in range(len(current_row)):

            if skip_rows > 0:
                skip_rows -= 1
                continue
            
            current_char = current_row[col]
            current_number = ''

            if current_char.isdigit():
                current_number += current_char
                skip_rows += 1
                i = 1
                while True:
                    if col + i > len(current_row) - 1:
                        break
                    test_test = current_row[col + i]

                    if test_test.isdigit():
                        current_number += test_test
                        skip_rows += 1
                    else:
                        break

                    i += 1
            
            # case number 
            if current_number != '':
                # print(current_number)
                for k in range(len(current_number)):  # do NOT subtract 1 from the range!
                    
                    star_coords = check_if_adjeacent_element_is_star(some_matrix=matrix, row=row, col=col + k)

                    for star_dict in star_coords:
                        current__star_row = star_dict['row']
                        current_col = star_dict['col']
                        print(f"Star dict; row: {current__star_row}; col: {current_col}")

                        if current__star_row not in star_indeces:
                            star_indeces[current__star_row] = {}
                            star_indeces[current__star_row][current_col] = [int(current_number)]
                        else:
                            if current_col not in star_indeces[current__star_row]:
                                star_indeces[current__star_row][current_col] = [int(current_number)]
                            else:
                                if int(current_number) not in star_indeces[current__star_row][current_col]:
                                    star_indeces[current__star_row][current_col].append(int(current_number))



print(star_indeces)

sum_of_gear_ratios: int = 0

for _, meta_dict in star_indeces.items():
    for current_list in meta_dict.values():
        if len(current_list) == 2:
            gear_ratio = current_list[0] * current_list[1]
            sum_of_gear_ratios += gear_ratio


print(f"The sum of gear ratios is: {sum_of_gear_ratios}")
