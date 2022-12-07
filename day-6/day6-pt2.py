with open('input.txt') as f:
    all_characters = list(f.read())
    found_marker = False
    current_list = []
    length_of_marker = 14

    for key, char in enumerate(all_characters):
        current_list = all_characters[key: key + length_of_marker: 1]

        for item in current_list:
            if current_list.count(item) > 1:
                break
            elif current_list.count(item) and current_list.index(item) == length_of_marker - 1:
                print("The answer is: ", key + length_of_marker)


