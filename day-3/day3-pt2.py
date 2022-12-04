import string

all_groups = []
group_badges = []
item_priority = list('0' + string.ascii_lowercase + string.ascii_uppercase)


with open('input.txt') as f:
    for line in f.read().split('\n'):
        all_groups.append(line)


for key, value in enumerate(all_groups):
    if key % 3 == 0:
        temp_badge_var = []
        for item in all_groups[key]:
            if item in all_groups[key + 1] and item in all_groups[key + 2] and item not in temp_badge_var:
                temp_badge_var.append(item)
        group_badges += temp_badge_var


print(f"All elf group badges: {group_badges}")


sum_of_priorities = sum([item_priority.index(item) for item in group_badges])


print(f"Sum of item priorities: {sum_of_priorities}")


