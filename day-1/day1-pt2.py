all_calories_per_elf = []
most_calories_per_elf = 0

with open('input.txt') as f:
    elf_values = [(elves.split('\n')) for elves in f.read().split('\n\n')]
    # elf_calories = [calories for elf in elf_values for calories in elf]
    # elf_totals = [sum(elf) for elf in elf_values]

print(elf_values)
# print(elf_totals)

# top_3_elves = sum(sorted(all_calories_per_elf)[-3:])

# print(f"top_3_elves: {top_3_elves}")
# print(f"Most calories per elf: {most_calories_per_elf}")