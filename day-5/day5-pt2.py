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

    print("Stacks list in original state: ", stacks_list)

    # move crates based on instructions

    for line in instructions.split('\n'):
        no_of_crates = int(line.split(' from ')[0].split(' ')[1])
        current_pos = int(line.split(' from ')[1].split(' ')[0]) - 1
        destination_pos = int(line.split(' to')[1]) - 1
        stacks = stacks_list

        # move one crate at a time, use a counter to loop based on number of crates to be moved

        crates_to_move = []

        for crate in range(no_of_crates):
            i = 0
            if no_of_crates == 1:
                crate_to_move = stacks[current_pos][0]
                stacks[current_pos].pop(0)
                stacks[destination_pos].insert(0, crate_to_move)
            elif no_of_crates > i:
                crates_to_move.append(stacks[current_pos][0])
                stacks[current_pos].pop(0)
                i += 1
        if crates_to_move:
            stacks[destination_pos] = crates_to_move + stacks[destination_pos]
        crates_to_move = []

print("Stacks list in final state: ", stacks)

top_of_stack = [stack[0] for stack in stacks]

print(f"Top of stack: {str(top_of_stack)}")
