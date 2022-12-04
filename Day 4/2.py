f = open('Day 4/input.txt')

totaal = 0

for x in f:
    x = x[:-1]
    x = x.split(',')
    x[0] = x[0].split('-')
    x[1] = x[1].split('-')
    x[0] = [int(y) for y in x[0]]
    x[1] = [int(y) for y in x[1]]
    print(x)

    range1 = range(x[0][0], x[0][1] + 1)
    range2 = range(x[1][0], x[1][1] + 1)

    for y in range1:
        if y in range2:
            totaal += 1
            break

print(totaal)