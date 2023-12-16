
test_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

my_file = open('input_15.txt')

real_input = my_file.read()

my_file.close()


def get_hash_value_of_string(some_string: str) -> int:

    hash_value: int = 0

    for char in some_string:
        char_ascii = ord(char)
        hash_value += char_ascii
        hash_value *= 17
        hash_value = hash_value % 256

    return hash_value


meta_shred = real_input.split(',')

total_res: int = 0

for string in meta_shred:
    current_has_value: int = get_hash_value_of_string(string)
    total_res += current_has_value

print(total_res)
