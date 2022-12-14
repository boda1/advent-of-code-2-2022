import string
directories = {}

with open('input.txt') as f:
    f_contents = f
    current_directory = ''
    current_file_weight = 0
    for key, line in enumerate(f_contents):
        line = line.strip()
        if line.startswith('$ cd') and '.' not in line:
            # add current file weight to all previous directories

            print("Line and file weight: ", line, current_file_weight, directories)

            for directory in directories:
                directories[directory] += current_file_weight
            current_file_weight = 0

            # add latest directory to dictionary of all directories

            if len(current_directory) > 1:
                current_directory += '/' + line.split('cd ')[1]
            else:
                current_directory += line.split('cd ')[1]
            directories[current_directory] = 0
            
            print("Line and file weight: ", line, current_file_weight, directories)
        elif line.startswith('$ cd') and '..' in line:
            # add directory to list

            directories[current_directory] = 0

            # add file weight to all directories

            for directory in directories:
                directories[directory] += current_file_weight
            current_file_weight = 0

            # update current directory to reflect having moved up one folder

            if len(current_directory) > 2:
                current_directory = current_directory[:-2]
            elif len(current_directory) <= 2:
                current_directory = current_directory[:-1]
        elif line[0].isdigit():
            current_file_weight += int(line.split(' ')[0])



print(directories)


"""
elif first_char.isdigit():
file_size = int(line.split(' ')[0])
total_file_size += file_size
# directories[current_directory] += file_size
"""