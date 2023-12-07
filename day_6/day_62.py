
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

split_times = [x.strip() for x in meta_split[0].split(':')[1].strip().split(' ') if x.strip() != '']
split_distances = [x.strip() for x in meta_split[1].split(':')[1].strip().split(' ') if x.strip() != '']

single_time = int(''.join(split_times))
single_distance = int(''.join(split_distances))

print(single_time, single_distance)

res = calculate_possible_times(single_time, single_distance)

print(f"Res is: {res}")
