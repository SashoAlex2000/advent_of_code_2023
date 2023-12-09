from math import gcd

import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(root_dir)

from utils.python_utils import file_reader, get_file_name_input_file

test_input = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

real_input = file_reader(get_file_name_input_file())

meta_shred = [x.strip() for x in real_input if x.strip() != '']

[print(x) for x in meta_shred]

instructions: str = meta_shred.pop(0)

dict_of_mappings: dict[str, list[str]] = {}
list_of_starting_coords: list[str] = []
ending_coords_dict = {}

for line in meta_shred:

    bits = line.split(' = ')
    node = bits[0].strip()
    # print(node)
    second = bits[1].split(',')
    left_instr = second[0].replace('(', '').strip()
    right_instr = second[1].replace(')', '').strip()
    
    dict_of_mappings[node] = [left_instr, right_instr]

    if node[-1] == 'A':
        list_of_starting_coords.append(node)

    if node[-1] == 'Z':
        ending_coords_dict[node] = -1

for k, v in dict_of_mappings.items():
    print(f"{k} -> {v}")

print(list_of_starting_coords)

turns_taken: int = 0
exit_found: bool = False
instr_index_counter = 0
curr_instruction = instructions[instr_index_counter]

current_node_names = [x for x in list_of_starting_coords]
current_nodes = [dict_of_mappings[x] for x in current_node_names]

while not exit_found:

    turns_taken += 1
    instr_index_counter += 1
    next_node_names = []
    next_nodes = []
    
    for cn in current_nodes:

        if curr_instruction == 'L':
            current_node_name = cn[0]
            current_node = dict_of_mappings[current_node_name]
        elif curr_instruction == 'R':
            current_node_name = cn[1]
            current_node = dict_of_mappings[current_node_name]

        next_node_names.append(current_node_name)
        next_nodes.append(current_node)


    if instr_index_counter >= len(instructions):
        instr_index_counter = 0

    curr_instruction = instructions[instr_index_counter]

    found_endings = 0

    for nd in next_node_names:
        if nd[-1] == 'Z':
            if ending_coords_dict[nd] < 0:
                ending_coords_dict[nd] = turns_taken
                found_endings += 1

    all_found = all([x >= 0 for x in list(ending_coords_dict.values())])

    if all_found:
        iterations_needed = list(ending_coords_dict.values())
        lcm = 1
        for i in iterations_needed:
            lcm = lcm*i//gcd(lcm, i)
        print(f"THE ANSWER IS: {lcm}")
        exit_found = True

    # print(f"Iterations: {turns_taken}")
    # time.sleep(1)
    
    if turns_taken % 100 == 0:
        print(f"Turns so far: {turns_taken}")

    current_node_names = next_node_names
    current_nodes = next_nodes
