from pprint import pprint
from functools import cmp_to_key

import os
import sys
from typing import Union

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(root_dir)

from utils.python_utils import file_reader, get_file_name_input_file

real_input = file_reader(get_file_name_input_file())

real_input = file_reader(get_file_name_input_file())


test_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

TYPES = ("five_of_a_kind", "four_of_a_kind", "full_house", "three_of_a_kind", "two_pairs", "one_pair", "high_card")
# ORDERING = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
ORDERING = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']  # NEW

# 1234J
# 123JJ
# 12JJJ
# 1JJJJ

# 1123J
# 112JJ
# 11JJJ

# 1112J
# 1111J

# 2211J
# 221JJ

def determine_card_hand_strength(hand):

    current_card_dict = {}

    jokers_present = 0

    for smbl in hand:
        if smbl == 'J':
            jokers_present += 1
            continue

        if smbl not in current_card_dict:
            current_card_dict[smbl] = 0
        current_card_dict[smbl] += 1

    if jokers_present > 0:

        if jokers_present == 5:
            return "five_of_a_kind"

        most_present_symbol = list(current_card_dict.keys())[0]
        max_times = current_card_dict[most_present_symbol]
        for sym, encounters in current_card_dict.items():
            if encounters > max_times:
                most_present_symbol = sym
        print(f"The most present symbol: {most_present_symbol}; times: {max_times}")
        current_card_dict[most_present_symbol] += jokers_present

    if len(current_card_dict) == 5:
        return "high_card"
    elif len(current_card_dict) == 4:
        return "one_pair"
    elif len(current_card_dict) == 3:
        # two pair or three of a kind
        for v in current_card_dict.values():
            if v == 3:
                return "three_of_a_kind"
        return "two_pairs"
    elif len(current_card_dict) == 2:
        # full house or four of a kind
        # TODO flip logic
        for value in current_card_dict.values():
            if value == 4 or value == 1:
                return "four_of_a_kind"
            return "full_house"
    elif len(current_card_dict) == 1:
        return "five_of_a_kind"


def custom_card_sort(card1, card2):
    card1_key = list(card1.keys())[0]
    card2_key = list(card2.keys())[0]
    exit = False

    for i in range(len(card1_key)):
        if ORDERING.index(card1_key[i]) > ORDERING.index(card2_key[i]):
            return -1
        elif ORDERING.index(card1_key[i]) < ORDERING.index(card2_key[i]):
            return 1
        else:
            continue

    return 0


# THIS IS WHAT WORKS FOR THE SORTING, MIMICKING THE JS array.sort((a,b) => ...)
# https://stackoverflow.com/questions/11850425/custom-python-list-sorting
custom_card_sort_key = cmp_to_key(custom_card_sort)

def sort_list_of_results(list_of_dicts):

    sorted_list = sorted(list_of_dicts, key=custom_card_sort_key)

    # new_dict = {k: some_dict[k] for k in keys}

    return sorted_list


# meta_shred = [x.strip() for x in test_input.split('\n') if x.strip() != '']
meta_shred = [x.strip() for x in real_input if x.strip() != '']

[print(x) for x in meta_shred]
TOTAL_LENGTH = len(meta_shred)
print(f"TOTAL LENGTH  is: {TOTAL_LENGTH}")
list_of_info_paris: list[list[str, str]] = []
TYPES_DICT = {x: [] for x in TYPES}
print(TYPES_DICT)

for line in meta_shred:
    shredded = line.split(' ')
    current_hand = shredded[0]
    current_bid = int(shredded[1])
    result_of_hand = determine_card_hand_strength(hand=current_hand)
    print(f"Hand: {current_hand}; Result: {result_of_hand}")
    TYPES_DICT[result_of_hand].append({current_hand: current_bid})

print(TYPES_DICT)
# pprint(TYPES_DICT)
t_res = sort_list_of_results(TYPES_DICT["three_of_a_kind"])
print(t_res)

iterations_passed = 0
total_score = 0

for type_of_hand, hand_dict in TYPES_DICT.items():
    list_of_sorted_dicts = sort_list_of_results(hand_dict)

    for sorted_dict in list_of_sorted_dicts:
        curr_b = list(sorted_dict.values())[0]
        current_result = curr_b * (TOTAL_LENGTH - iterations_passed)
        print(f"CURRENT CARD: {list(sorted_dict.keys())[0]} - {current_result}")
        total_score += current_result
        iterations_passed += 1


print(f"FINAL SCORE: {total_score}")

