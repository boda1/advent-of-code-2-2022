my_score = 0


with open('input.txt') as f:
    games = f.read().split('\n')
    for game in games:
        opponent_choice = game.split(' ')[0]
        my_choice = game.split(' ')[1]
        if opponent_choice == 'A' and my_choice == 'X':
            my_score += 4
        elif opponent_choice == 'A' and my_choice == 'Y':
            my_score += 8
        elif opponent_choice == 'A' and my_choice == 'Z':
            my_score += 3
        elif opponent_choice == 'B' and my_choice == 'X':
            my_score += 1
        elif opponent_choice == 'B' and my_choice == 'Y':
            my_score += 5
        elif opponent_choice == 'B' and my_choice == 'Z':
            my_score += 9
        elif opponent_choice == 'C' and my_choice == 'X':
            my_score += 7
        elif opponent_choice == 'C' and my_choice == 'Y':
            my_score += 2
        elif opponent_choice == 'C' and my_choice == 'Z':
            my_score += 6
        else:
            print("A combination has been missed")


print(my_score)


"""
A = rock
B = paper
C = scissors

X = rock = 1
Y = paper = 2
Z = scissors = 3

win = 6
draw = 3
loss = 0

"""