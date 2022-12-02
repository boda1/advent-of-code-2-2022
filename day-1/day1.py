all_calories_per_elf = []
most_calories_per_elf = 0

with open('input.txt') as f:
    current_total = 0
    for line in f.readlines():
        if line != '\n':
            current_total += int(line)
        else:
            all_calories_per_elf.append(current_total)
            current_total = 0
    all_calories_per_elf.append(current_total)


for calories_per_elf in all_calories_per_elf:
    if most_calories_per_elf < calories_per_elf:
        most_calories_per_elf = calories_per_elf


print(f"Most calories per elf: {most_calories_per_elf}")