import string

with open("input.txt") as f:
    lines = f.readlines()
    items = [item.replace("\n", "") for item in lines]

lookup = list(string.ascii_lowercase) + list(string.ascii_uppercase)

priority_sum = 0

for item in items:
    comp_1 = list(item)[:int(len(item)/2)]
    comp_2 = list(item)[int(len(item)/2):]

    diff = list(set(comp_1) & set(comp_2))

    if len(diff) > 0:
        priority_sum += lookup.index(diff[0]) + 1

part_1_answer = priority_sum
print(part_1_answer)


priority_sum_part_2 = 0
n_in_group = 0
group_bags = []

for item in items:
    n_in_group += 1
    group_bags.append(item)

    if n_in_group == 3:
        diff = list(set(group_bags[0]) & set(
            group_bags[1]) & set(group_bags[2]))
        priority_sum_part_2 += lookup.index(diff[0]) + 1

        # Reset group values for next group
        n_in_group = 0
        group_bags = []

part_2_answer = priority_sum_part_2
print(part_2_answer)
