
test_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

FILE_NAME: str = 'input_2.txt'
main_input: list[str] = []

with open(FILE_NAME, 'r') as f:
    for line in f:
        main_input.append(line.rstrip())
    

COLOR_TUPLE = (
    "red",
    "green",
    "blue",
)

SUM_OF_SET_POWERS: int = 0

for line in main_input:

    current_dict = {
        "blue": 0,
        "red": 0,
        "green": 0,
    }

    info_sets = [x.strip() for x in line.split(':')[1].split(';')]

    for info_set in info_sets:

        shredded = [x.strip() for x in info_set.split(',')]

        for shrd in shredded:

            [number, color] = shrd.split(' ')

            if color not in current_dict:
                print("?!?!?!?!?!?")
            else:
                if current_dict[color] < int(number):
                    current_dict[color] = int(number)

    current_set_power = 1 if all([x > 0 for x in current_dict.values()]) else 0

    for ccolor in COLOR_TUPLE:
        current_set_power *= current_dict[ccolor]

    SUM_OF_SET_POWERS += current_set_power

print(f"The total set power is: {SUM_OF_SET_POWERS}")  # 69929
