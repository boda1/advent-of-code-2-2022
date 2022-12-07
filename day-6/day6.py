with open('input.txt') as f:
    all_characters = list(f.read())
    found_marker = False

    for key, char in enumerate(all_characters):
            char1 = all_characters[key]
            char2 = all_characters[key + 1]
            char3 = all_characters[key + 2]
            char4 = all_characters[key + 3]

            print(char1, char2, char3, char4)

            if char1 != char2 and char1 != char3 and char1 != char4 and char2 != char3 and char2 != char4 and char3 != char4:
                print("The answer: ", key + 3 + 1)
                break
