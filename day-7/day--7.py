directories = []
dir_file_weights = []
file_weight_running_total = 0

with open('input.txt') as f:
    f_contents = f
    current_directory = ''

    # create list of all directories

    for key, line in enumerate(f_contents):
        line = line.strip()
        if line.startswith('$ cd') and '.' not in line:

            # add running total of files to all prev file weights in list

            dir_file_weights.append(0)
            for key, item in enumerate(dir_file_weights):
                dir_file_weights[key] += file_weight_running_total
            file_weight_running_total = 0

            # add new directory to list of directories

            current_directory = line.split('cd ')[1]
            directories.append(current_directory)

        elif line.startswith('$ cd') and '..' in line:

            for key_1, item in enumerate(dir_file_weights):
                dir_file_weights[key_1] += file_weight_running_total
            file_weight_running_total = 0

        elif line[0].isdigit():
            file_weight_running_total += int(line.split(' ')[0])

    for key_2, item in enumerate(dir_file_weights):
        dir_file_weights[key_2] += file_weight_running_total
    file_weight_running_total = 0




print(directories)
print(dir_file_weights)
