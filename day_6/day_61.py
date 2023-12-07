
def calculate_possible_times(t_time, record_distance):

    record_breaking_times: int = 0

    for charge_time in range(t_time):
        speed_achieved = charge_time
        time_racing = t_time - charge_time

        current_distance_traveled = speed_achieved * time_racing

        # print(f"Charged for: {charge_time}, achieved: {speed_achieved}, left time to race: {time_racing}, traveled: {current_distance_traveled}")

        if current_distance_traveled > record_distance:
            record_breaking_times += 1

    return record_breaking_times


test_input = """
Time:      7  15   30
Distance:  9  40  200
"""

real_input = """
Time:        35     93     73     66
Distance:   212   2060   1201   1044
"""

meta_split = [x for x in real_input.split('\n') if x.strip() != '']

print(meta_split)

split_times = [int(x.strip()) for x in meta_split[0].split(':')[1].strip().split(' ') if x.strip() != '']
split_distances = [int(x.strip()) for x in meta_split[1].split(':')[1].strip().split(' ') if x.strip() != '']

list_of_pairs = [[split_times[i], split_distances[i]] for i in range(len(split_times))]
print(list_of_pairs)

total_error_multiplier = 0

for info_pair in list_of_pairs:
    
    res: int = calculate_possible_times(info_pair[0], info_pair[1])
    
    if total_error_multiplier == 0:
        total_error_multiplier = 1

    total_error_multiplier *= res

print(total_error_multiplier)

