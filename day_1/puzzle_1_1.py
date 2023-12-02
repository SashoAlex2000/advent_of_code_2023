
test_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

# test read
FILE_NAME: str = 'input_1.txt'
main_input: list[str] = []

with open(FILE_NAME, 'r') as f:
    for line in f:
        main_input.append(line.rstrip())
    

def calculate_string_number(some_string):
    list_of_ints = [int(s) for s in list(some_string) if s.isdigit()]

    if len(list_of_ints) == 0:
        print("ZERO LIST ???")
        return None

    if len(list_of_ints) == 1:
        return str(list_of_ints[0]) + str(list_of_ints[0])

    return str(list_of_ints[0]) + str(list_of_ints[-1])


final_result = 0

for text in main_input:
    if text.strip() != '':
        res = calculate_string_number(text)
        final_result += int(res)

print(f"The final result is: {final_result}")  # 54632
