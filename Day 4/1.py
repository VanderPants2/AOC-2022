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

    if x[0][0] <= x[1][0] and x[0][1] >= x[1][1]:
        totaal += 1
    elif x[1][0] <= x[0][0] and x[1][1] >= x[0][1]:
        totaal += 1

print(totaal)