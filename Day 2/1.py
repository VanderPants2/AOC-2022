f = open('Day 2/test_input.txt')

totalScore = 0
roundScore = 0

score = {
    0: {
        'A': 1,
        'B': 2,
        'C': 3
    },
    1: {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
}

'''
A - X -> Rock
B - Y -> Paper
C - Z - Scissors
'''

for x in f:
    x = x.split(' ')
    x[1] = x[1][:-1]

    if x[0] == 'A':
        if x[1] == 'X':
            roundScore += 3
        elif x[1] == 'Y':
            roundScore += 6
        else:
            pass
    elif x[0] == 'B':
        if x[1] == 'X':
            pass
        elif x[1] == 'Y':
            roundScore += 3
        else:
            roundScore += 6
    else:
        if x[1] == 'X':
            roundScore += 6
        elif x[1] == 'Y':
            pass
        else:
            roundScore += 3

    roundScore += score[1][x[1]]
    totalScore += roundScore
    roundScore = 0

print(totalScore)
