my_score = 0
scores = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}


with open('input.txt') as f:
    games = f.read().split('\n')
    my_score = sum([scores[game] for game in games])


print(my_score)


"""
A = rock
B = paper
C = scissors

X = lose
Y = draw
Z = win

rock = 1
paper = 2
scissors = 3

win = 6
draw = 3
loss = 0

"""


