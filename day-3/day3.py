import string

found_in_both = []
item_priority = list('0' + string.ascii_lowercase + string.ascii_uppercase)
sum_of_priorities = 0


with open('input.txt') as f:
    for line in f.read().split('\n'):
        matching_chars_in_line = []
        half_line_length = int(len(line)/2)
        first_half = list(line)[:half_line_length]
        second_half = list(line)[half_line_length:]
        # print(first_half)
        # print(second_half)
        for char in first_half:
            if char in second_half and char not in matching_chars_in_line:
                matching_chars_in_line.append(char)
        found_in_both += matching_chars_in_line


for item in found_in_both:
    sum_of_priorities += item_priority.index(item)


print(found_in_both)
print(sum_of_priorities)