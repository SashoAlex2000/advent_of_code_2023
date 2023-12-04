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


def is_element_symbol(element):

    if element is None:  # important
        return False

    if not element.isdigit() and element != '.':
        return True
    
    return False



def check_if_adjeacent_element_is_symbol(some_matrix, row, col) -> bool:

    diagonal_up_left = get_by_index_or_None(some_matrix=some_matrix, row=row-1, col=col-1)
    if is_element_symbol(diagonal_up_left): return True
    
    up = get_by_index_or_None(some_matrix=some_matrix, row=row-1, col=col)
    if is_element_symbol(up): return True

    diagonal_up_right = get_by_index_or_None(some_matrix=some_matrix, row=row-1, col=col + 1)
    if is_element_symbol(diagonal_up_right): return True

    left_adjacent = get_by_index_or_None(some_matrix=some_matrix, row=row, col=col - 1)
    if is_element_symbol(left_adjacent): return True

    right_adjacent = get_by_index_or_None(some_matrix=some_matrix, row=row, col=col + 1)
    if is_element_symbol(right_adjacent): return True

    diagonal_down_right = get_by_index_or_None(some_matrix=some_matrix, row=row+1, col=col - 1)
    if is_element_symbol(diagonal_down_right): return True

    down = get_by_index_or_None(some_matrix=some_matrix, row=row+1, col=col)
    if is_element_symbol(down): return True

    diagonal_down_left = get_by_index_or_None(some_matrix=some_matrix, row=row+1, col=col + 1)
    if is_element_symbol(diagonal_down_left): return True

    return False


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
                    flag = check_if_adjeacent_element_is_symbol(some_matrix=matrix, row=row, col=col + k)

                    if flag:
                        total_sum += int(current_number)  # parse to int just here
                        # print(f"VALID NUMBER: {current_number}")
                        break


print(f"The final sum is: {total_sum}")

