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

def get_by_index_or_None(some_matrix: list[list[str]], row: int, col: int) -> Union[str, int, None]:

    if row < 0 or row > len(some_matrix) - 1:
        return None
    
    correct_row = some_matrix[row]

    if col < 0 or col > len(correct_row) - 1:
        return None
    
    return int(correct_row[col]) if correct_row[col].isdigit() else correct_row[col]


def get_adjacent_number_from_matrix_index(some_matrix, row, col):

    current_numbers: list[Union[int, None]] = []

    diagonal_up_left = get_by_index_or_None(some_matrix=some_matrix, row=row-1, col=col-1)
    
    current_numbers.append(diagonal_up_left)

    up = get_by_index_or_None(some_matrix=some_matrix, row=row-1, col=col)
    current_numbers.append(up)

    diagonal_up_right = get_by_index_or_None(some_matrix=some_matrix, row=row-1, col=col + 1)
    current_numbers.append(diagonal_up_right)

    left_adjacent = get_by_index_or_None(some_matrix=some_matrix, row=row, col=col - 1)
    current_numbers.append(left_adjacent)

    right_adjacent = get_by_index_or_None(some_matrix=some_matrix, row=row, col=col + 1)
    current_numbers.append(right_adjacent)

    diagonal_down_right = get_by_index_or_None(some_matrix=some_matrix, row=row+1, col=col - 1)
    current_numbers.append(diagonal_down_right)

    down = get_by_index_or_None(some_matrix=some_matrix, row=row+1, col=col)
    current_numbers.append(down)

    diagonal_down_left = get_by_index_or_None(some_matrix=some_matrix, row=row+1, col=col + 1)
    current_numbers.append(diagonal_down_left)

    res: int = sum(filter(lambda i: isinstance(i, int), current_numbers))
    print(f"Current sum is {res} for {current_numbers}")
    return res


lines: list[str] = [x for x in test_input.split('\n') if x.strip() != '']
matrix = [list(line) for line in lines]

# [print(x) for x in matrix]

def print_matrix(p_matrix):
    for row in range(len(p_matrix) - 1):
        for col in range(len(p_matrix[row]) - 1):
            print(p_matrix[row][col], end=' ')
        print('\n')


print_matrix(p_matrix=matrix)

for row in range(len(matrix) - 1):
        for col in range(len(matrix[row]) - 1):
            current_char = matrix[row][col]

            if not current_char.isdigit() and current_char != '.':
                current_sum = get_adjacent_number_from_matrix_index(
                    some_matrix=matrix,
                    row=row,
                    col=col,
                )

                print(current_sum)

