import os
from typing import Union

# have to use Union in type hints, '|' available after python 3.10 ...
def file_reader(path_to_file: str) -> Union[list[str], None]:  
    

    if not os.path.isfile(path_to_file):
        print(f"Path to file: {path_to_file} is wrong!")
        return None 

    result: list[str] = []

    with open(path_to_file, 'r') as f:
        for line in f:
            result.append(line.rstrip())

    return result


def get_file_name_input_file() -> Union[str, None]:

    # This assumes only one input file in the current directory

    current_files = os.listdir()

    for file in current_files:
        if 'input' in file:
            return file
    
    print("No file with 'input' in current directory")
    return None

