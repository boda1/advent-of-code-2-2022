stacks_list = []

with open('input.txt') as f:
    file_contents = f.read()
    stacks = file_contents.split(' 1   2   3')[0].replace('    ', '-').replace('[', '').replace(']', '').replace(' ', '').split('\n')
    instructions = file_contents.split('\n\n')[1]
    no_of_stacks = int(file_contents.split('\n\n')[0].split(' ')[-2])

    # create list-of-lists equal to length of stacks

    for i in range(no_of_stacks):
        stacks_list.append([])

    # populate nested lists with characters from stacks

    for line in stacks:
        if len(line) < 3:
            line += '-'
        for key, char in enumerate(line):
            if char != '-':
                stacks_list[key].append(char)

    # move crates based on instructions

    for line in instructions.split('\n'):
        no_of_crates = int(line.split(' from ')[0].split(' ')[1])
        current_pos = int(line.split(' from ')[1].split(' ')[0]) - 1
        destination_pos = int(line.split(' to')[1]) - 1
        reordered_stacks = stacks_list

        # move one crate at a time

        for crate in range(no_of_crates):
            crate_to_move = reordered_stacks[current_pos][0]
            reordered_stacks[current_pos].pop(0)
            reordered_stacks[destination_pos].insert(0, crate_to_move)

top_of_stack = []

for stack in reordered_stacks:
    top_of_stack.append(stack[0])

print(str(top_of_stack))
