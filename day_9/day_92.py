import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(root_dir)

from utils.python_utils import file_reader, get_file_name_input_file

test_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

def get_first_difference_of_row(some_row: list[int]) -> list[int]:
    
    new_list = []
    
    for i in range(0, len(some_row) - 1, 1):
        new_list.append(some_row[i+1] - some_row[i])

    flag = all([x == 0 for x in new_list])
    if flag:
        return new_list

    new_value_row_below = get_first_difference_of_row(new_list)[0]
    value_to_add = new_list[0] - new_value_row_below
    new_list.insert(0, value_to_add)

    return new_list


def calculate_next_integer(row: list[int]) -> int:
    
    result_list: list[int] = get_first_difference_of_row(row)

    inner_res = row[0] - result_list[0]

    return inner_res


# meta_shred = [[int(y) for y in x.strip().split(' ')] for x in real_input.split('\n') if x .strip() != '']
meta_shred = [[int(y) for y in x.strip().split(' ')] for x in file_reader(get_file_name_input_file()) if x .strip() != '']


sum_of_predictions = 0

for line in meta_shred:
    current_next_integer: int = calculate_next_integer(line)
    print(f"Current next int is: {current_next_integer}")
    sum_of_predictions += current_next_integer

print(f"The total sum of predictions is: {sum_of_predictions}")
