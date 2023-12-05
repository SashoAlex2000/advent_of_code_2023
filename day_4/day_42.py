import os
import sys
from typing import Union

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(root_dir)

from utils.python_utils import file_reader, get_file_name_input_file

# test input 
# test_input: str = """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """
# lines: list[str] = [x for x in test_input.split('\n') if x.strip() != '']

# full input
FILE_NAME = get_file_name_input_file()
main_input = file_reader(FILE_NAME)
lines: list[str] = [x for x in main_input if x.strip() != '']

[print(x) for x in lines]

dict_of_scratchcard_occurances = {i: 1 for i in range(len(lines))}
total_scratch_cards_won: int = 0

for index, line in enumerate(lines):
    
    nums_part = line.split(':')[1].strip()

    shredded = nums_part.split(' | ')
    winning_numbers = [int(x.strip()) for x in shredded[0].split(' ') if x.strip() != '']
    current_numbers = [int(x.strip()) for x in shredded[1].split(' ') if x.strip() != '']

    current_matches_amount : int = 0
    current_copy_power = dict_of_scratchcard_occurances[index]

    for curr in current_numbers:
        
        if curr in winning_numbers:
            current_matches_amount += 1

    if current_matches_amount > 0:
        for k in range(index + 1, index + 1 + current_matches_amount):
            dict_of_scratchcard_occurances[k] += 1 * current_copy_power


print(dict_of_scratchcard_occurances)

print(f"Total amount of scratchcards: {sum([x for x in dict_of_scratchcard_occurances.values()])}")
