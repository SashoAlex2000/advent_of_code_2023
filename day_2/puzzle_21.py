
test_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


# puzzles
# collect info regarding the games - dicts with colors and how many times they've appeared. -> Summing them is wrong ... -> just collect it as max
# later check for each whether it is valid

FILE_NAME: str = 'input_2.txt'
main_input: list[str] = []

with open(FILE_NAME, 'r') as f:
    for line in f:
        main_input.append(line.rstrip())
    

split_input = main_input

dict_of_results: dict[int, dict[str, int]] = {}
game_counter: int = 0

for line in main_input:

    current_dict = {  # The int is the MAX cubes pulled out from a subset
        "blue": 0,
        "red": 0,
        "green": 0,
    }

    game_counter += 1
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

    dict_of_results[game_counter] = current_dict


CONDITION = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

COLOR_TUPLE = (
    "red",
    "green",
    "blue",
)

SUM_OF_VALID_KEYS: int = 0

for game_id, color_dict in dict_of_results.items():

    flag = True

    for color in COLOR_TUPLE:
        if CONDITION[color] < color_dict[color]:
            # print(f"For game with ID: {game_id}; breaking at color: {color}")
            flag = False
            break

    if flag:
        SUM_OF_VALID_KEYS += game_id


print(f"The sum of the valid game IDs: {SUM_OF_VALID_KEYS}")  # Correct answer 2164


