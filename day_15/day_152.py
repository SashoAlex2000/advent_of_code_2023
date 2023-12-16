

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


# meta_shred = test_input.split(',')
meta_shred = real_input.split(',')

print(get_hash_value_of_string('qp'))

total_res: int = 0

# map_of_lenses = {i: {k: '' for k in range(1,10)} for i in range(257)}
map_of_lenses: dict[int, list[str]] = {i: [] for i in range(257)}
# for k, v in map_of_lenses.items():
#     print(f'{k} -> {v}')


for string in meta_shred:

    if '=' in string:
        bits = string.split('=')
        current_label = bits[0]
        current_box = get_hash_value_of_string(current_label)

        full_string = f"{current_label} {bits[1]}"

        if current_box not in map_of_lenses:
            assert False

        lens_is_present: bool = False
        list_curr = map_of_lenses[current_box]
        for indx, present_lens in enumerate(list_curr):
            if current_label in present_lens:
                lens_is_present = True
                list_curr[indx] = full_string
                break

        if not lens_is_present:
            list_curr.append(full_string)

        map_of_lenses[current_box] = list_curr

    elif '-' in string:
        bits = string.split('-')
        label = bits[0]

        current_box = get_hash_value_of_string(label)

        list_curr = map_of_lenses[current_box]

        for indx, lens in enumerate(list_curr):
            if label in lens:
                list_curr.pop(indx)
                break

        map_of_lenses[current_box] = list_curr

    else:
        assert False


total_power: int = 0

for k, v in map_of_lenses.items():
    box_weight = k + 1

    for pos, lens in enumerate(v):
        slot_weight = pos + 1
        focal_length = int(lens.split(' ')[1])

        current_focusing_power = box_weight * slot_weight * focal_length
        total_power += current_focusing_power

print(f"Total focusing power: {total_power}")

