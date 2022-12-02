f = open('Day 2/input.txt')

totalScore = 0
roundScore = 0

score = {
    0: {
        'A': 1,
        'B': 2,
        'C': 3
    },
    1: {
        'X': 0,
        'Y': 3,
        'Z': 6
    }
}

'''
A -> Rock
B -> Paper
C -> Scissors
'''
'''
X -> Lose
Y -> Draw
Z -> Win
'''

for x in f:
    x = x.split(' ')
    x[1] = x[1][:-1]

    if x[0] == 'A':
        if x[1] == 'X':
            roundScore += 3
        elif x[1] == 'Y':
            roundScore += 1
        else:
            roundScore += 2
    elif x[0] == 'B':
        if x[1] == 'X':
            roundScore += 1
        elif x[1] == 'Y':
            roundScore += 2
        else:
            roundScore += 3
    else:
        if x[1] == 'X':
            roundScore += 2
        elif x[1] == 'Y':
            roundScore += 3
        else:
            roundScore += 1

    roundScore += score[1][x[1]]
    totalScore += roundScore
    roundScore = 0

print(totalScore)
