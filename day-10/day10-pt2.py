previous_cycles = 0
cycles = 0
previous_x = 0
X = 1
sum_of_signals = 0


def calc_signals_prev(prev_x, current_cycles):
    return prev_x * current_cycles


def calc_signals(current_x, current_cycles):
    return current_x * current_cycles


with open('input.txt') as f:
    for instruction in f:
        if instruction.startswith('addx'):
            no_to_add = int(instruction.split(' ')[1])

            # Addition instructions: split line finding number to be added,
            # increment number of cycles by 2, add number to X

            previous_cycles = cycles
            cycles += 2
            previous_x = X
            X += no_to_add
        elif instruction.startswith('noop'):

            # Do nothing other than increment number of cycles

            previous_x = X
            previous_cycles = cycles
            cycles += 1
        cycles_since_instruction = cycles - previous_cycles

        for c in [20, 60, 100, 140, 180, 220]:
            if previous_cycles < c < cycles or cycles == c and cycles_since_instruction <= 2:
                sum_of_signals += calc_signals_prev(previous_x, c)
            elif cycles == c:
                sum_of_signals += calc_signals(X, c)


print(sum_of_signals)
