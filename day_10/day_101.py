
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(root_dir)

from utils.python_utils import file_reader, get_file_name_input_file

from itertools import combinations

def print_matrix(p_matrix):
    for r in range(len(p_matrix)):
        for c in range(len(p_matrix[r])):
            print(p_matrix[r][c], end=' ')
        print("\n")


real_input = file_reader(get_file_name_input_file())

simple_test_input = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

complex_test_input = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

DIRECTIONS_MAPS = {
    '|': {
        'north': {
            'row': 'plus',
            'col': 'same',
        },
        'south': {
            'row': 'minus',
            'col': 'same',
        },
        'meta': 'same'
    },
    '-': {
        'east': {
            'row': 'same',
            'col': 'minus',
        },
        'west': {
            'row': 'same',
            'col': 'plus',
        },
        'meta': 'same'
    },
    'L': {
        'north': {
            'row': 'same',
            'col': 'plus',
        },
        'east': {
            'row': 'minus',
            'col': 'same',
        },
        'meta': {
            'north': 'west',
            'east': 'south',
        }
    },
    'J': {
        'north': {
            'row': 'same',
            'col': 'minus',
        },
        'west': {
            'row': 'minus',
            'col': 'same',
        },
        'meta': {
            'north': 'east',
            'west': 'south',
        },
    },
    '7': {
        'south': {
            'row': 'same',
            'col': 'minus',
        },
        'west': {
            'row': 'plus',
            'col': 'same',
        },
        'meta': {
            'south': 'east',
            'west': 'north',
        }
    },
    'F': {
        'south': {
            'row': 'same',
            'col': 'plus',
        },
        'east': {
            'row': 'plus',
            'col': 'same',
        },
        'meta': {
            'south': 'west',
            'east': 'north',
        }
    },

}


# meta_shred = [[y for y in list(x.strip())] for x in test_input.split("\n") if x.strip() != '']
meta_shred = [[y for y in list(x.strip())] for x in real_input if x.strip() != '']

[print(x) for x in meta_shred]


class PipeCrawler:

    DIR_MAP = DIRECTIONS_MAPS
    MATRIX = meta_shred

    def __init__(self, name, row, col, came_from) -> None:
        self.name = name
        self.__turns_taken: int = 0
        self.row = row
        self.col = col
        # self.direction = direction
        self.came_from = came_from
        self.current_symbol = self.MATRIX[self.row][self.col]


    def get_next_pos(self):

        if self.current_symbol == '.':
            return False

        next_row: int = self.row
        next_col: int = self.col
        new_came_from: str
        
        current_symbol_map = self.DIR_MAP[self.current_symbol]
        try:
            dir_map = current_symbol_map[self.came_from]
        except KeyError:
            return False

        next_row_direction = dir_map["row"]
        next_col_direction = dir_map["col"]

        if next_row_direction == "plus":
            next_row += 1
        elif next_row_direction == 'minus':
            next_row -= 1

        if next_col_direction == "plus":
            next_col += 1
        elif next_col_direction == 'minus':
            next_col -= 1

        meta_dir = current_symbol_map["meta"]

        if meta_dir == "same":
            new_came_from = self.came_from
        else:
            new_came_from = meta_dir[self.came_from]

        # print(f"Next row: {next_row}; Next col: {next_col}")

        self.row= next_row
        self.col = next_col
        self.came_from = new_came_from

        self.current_symbol = self.MATRIX[self.row][self.col]

        if self.current_symbol == 'S':
            return 'S'

        self.__turns_taken += 1

        return True

        # return (next_row, next_col)

    def print_self_pos(self):

        print(f"Name: {self.name}; Row: {self.row}; Col: {self.col}; Travelling from: {self.came_from}; Turns taken: {self.__turns_taken}; Current symbol: {self.current_symbol}")

    def get_turns_taken(self):
        return self.__turns_taken
    
    def __eq__(self, other):
        if isinstance(other, PipeCrawler):
            return self.row == other.row and self.col == other.col
        return False


animal_row: int = -1
animal_col: int = -1

print_matrix(meta_shred)

for r in range(len(meta_shred)):
    for c in range(len(meta_shred[r])):
        if meta_shred[r][c] == 'S':
            animal_row = r
            animal_col = c
            break

    if animal_col > 0:
        break

print(animal_row, animal_col)


east_crawler = PipeCrawler(name="east_crawler", row=animal_row, col=animal_col+1,came_from='west')
south_crawler = PipeCrawler(name="south_crawler", row=animal_row+1, col=animal_col, came_from='north')
north_crawler = PipeCrawler(name="north_crawler", row=animal_row-1, col=animal_col, came_from='south')
west_crawler = PipeCrawler(name="west_crawler", row=animal_col, col=animal_col-1, came_from='east')

list_of_crawlers = [north_crawler, south_crawler, east_crawler, west_crawler]

end_pos_found = False
start_pos_found = False

answers = []

for crawler in list_of_crawlers:

    while True:
        # time.sleep(1)
        flag = crawler.get_next_pos()
        if flag == False:
            print(f"Going to new crawler")
            break
        if flag == 'S':
            print(f"The start has been reached by: {crawler.name}")
            print(f"The total turns to the start are: {crawler.get_turns_taken()}")
            answer = int((crawler.get_turns_taken() / 2) + 1)
            print(f"Answer is: {answer}")
            answers.append(answer)
            break
    
[print(a) for a in answers]  # why are the answers different ?

