import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(root_dir)

from utils.python_utils import file_reader, get_file_name_input_file


test_input = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

test_input_2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

real_input = file_reader(get_file_name_input_file())

meta_shred = [x.strip() for x in real_input if x.strip() != '']

[print(x) for x in meta_shred]

instructions: str = meta_shred.pop(0)

dict_of_mappings: dict[str, list[str]] = {}

for line in meta_shred:

    bits = line.split(' = ')
    node = bits[0].strip()
    # print(node)
    second = bits[1].split(',')
    left_instr = second[0].replace('(', '').strip()
    right_instr = second[1].replace(')', '').strip()
    
    dict_of_mappings[node] = [left_instr, right_instr]

for k, v in dict_of_mappings.items():
    print(f"{k} -> {v}")


turns_taken: int = 0

exit_found: bool = False
curr_instruction = instructions[0]
current_node_name = 'AAA'
current_node = dict_of_mappings[current_node_name]
instr_index_counter = 0


while not exit_found:

    turns_taken += 1
    instr_index_counter += 1
    print(f"Current node name: {current_node_name}")
    print(f"current node {current_node}")
    if curr_instruction == 'L':
        current_node_name = current_node[0]
        current_node = dict_of_mappings[current_node_name]
    elif curr_instruction == 'R':
        current_node_name = current_node[1]
        current_node = dict_of_mappings[current_node_name]

    print(f"Current instrunction {curr_instruction}")
    print(f"Next node: {current_node}")

    if instr_index_counter >= len(instructions):
        instr_index_counter = 0

    curr_instruction = instructions[instr_index_counter]

    if current_node_name == 'ZZZ':
        print(f"Exit reached after: {turns_taken} turns!")
        break
