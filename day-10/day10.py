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

            print("Instruction: ", instruction, "Value of X: ", X, "Number of cycles: ", cycles)
        elif instruction.startswith('noop'):

            # Do nothing other than increment number of cycles

            previous_x = X
            previous_cycles = cycles
            cycles += 1
            # print("Value of X: ", X, "Number of cycles: ", cycles)

        cycles_since_instruction = cycles - previous_cycles

        if previous_cycles < 20 < cycles or cycles == 20 and cycles_since_instruction <= 2:
            sum_of_signals += calc_signals_prev(previous_x, 20)
        elif cycles == 20:
            sum_of_signals += calc_signals(X, 20)
        elif previous_cycles < 60 < cycles or cycles == 60 and cycles_since_instruction <= 2:
            sum_of_signals += calc_signals_prev(previous_x, 60)
        elif cycles == 60:
            sum_of_signals += calc_signals(X, 60)
        elif previous_cycles < 100 < cycles or cycles == 100 and cycles_since_instruction <= 2:
            sum_of_signals += calc_signals_prev(previous_x, 100)
            print("State at 100: ", previous_cycles, cycles, previous_x, X)
        elif cycles == 100:
            sum_of_signals += calc_signals(X, 100)
        elif previous_cycles < 140 < cycles or cycles == 140 and cycles_since_instruction <= 2:
            sum_of_signals += calc_signals_prev(previous_x, 140)
        elif cycles == 140:
            sum_of_signals += calc_signals(X, 140)
        elif previous_cycles < 180 < cycles or cycles == 180 and cycles_since_instruction <= 2:
            sum_of_signals += calc_signals_prev(previous_x, 180)
        elif cycles == 180:
            sum_of_signals += calc_signals(X, 180)
        elif previous_cycles < 220 < cycles or cycles == 220 and cycles_since_instruction <= 2:
            sum_of_signals += calc_signals_prev(previous_x, 220)
        elif cycles == 220 and cycles_since_instruction > 2:
            sum_of_signals += calc_signals(X, 220)


print(sum_of_signals)
