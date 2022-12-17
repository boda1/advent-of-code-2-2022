cycles = 0
X = 1
sum_of_signals = 0


def check_cycle():
    if cycles in [20, 60, 100, 140, 180, 220]:
        return X * cycles
    return 0


with open('input.txt') as f:
    for instruction in f:
        cycles += 1
        sum_of_signals += check_cycle()
        if instruction.startswith('addx'):
            no_to_add = int(instruction.split(' ')[1])
            cycles += 1
            sum_of_signals += check_cycle()
            X += no_to_add


print(sum_of_signals)
