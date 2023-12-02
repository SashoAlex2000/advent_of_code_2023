
test_input = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

"""

char_num_to_int = {  # No zero!
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

FILE_NAME: str = 'input_1.txt'
main_input: list[str] = []

with open(FILE_NAME, 'r') as f:
    for line in f:
        main_input.append(line.rstrip())


def calculate_string_number_modified(some_string):

    list_of_number_chars_included = []

    # list_of_ints = [int(s) for s in list(some_string) if s.isdigit()]

    for index, char in enumerate(some_string):  # index first in enumerate

        if char.isdigit():
            list_of_number_chars_included.append(char)
            # print(f"Found a number: {char}")
        else:

            inner_meta_word = ''

            for i in range(index, len(some_string)):
                inner_meta_word += some_string[i]
                # print(inner_meta_word)
                if inner_meta_word in char_num_to_int:
                    # print(f"Found meta word: {inner_meta_word}")
                    list_of_number_chars_included.append(char_num_to_int[inner_meta_word])
                    break

    if len(list_of_number_chars_included) == 0:
        print("ZERO LIST ???")
        return None

    if len(list_of_number_chars_included) == 1:
        return str(list_of_number_chars_included[0]) + str(list_of_number_chars_included[0])

    return str(list_of_number_chars_included[0]) + str(list_of_number_chars_included[-1])


list_of_texts = main_input

final_result = 0

for text in list_of_texts:
    if text.strip() != '':
        res = calculate_string_number_modified(text)
        # print(res)
        final_result += int(res)

print(f"The final result is: {final_result}")  # 54019
