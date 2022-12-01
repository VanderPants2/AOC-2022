# > 197833
# 199172

f = open('Day 1/input.txt')

big = [0, 0, 0]
som = 0

for x in f:
    if x != '\n':
        som += int(x[:-1])
    else:
        if big[0] < som:
            big[0] = som
        elif big[1] < som:
            big[1] = som
        elif big[2] < som:
            big[2] = som
        som = 0
        big.sort(reverse=False)
        print(big)

print(big)
total = sum(big)
print(total)
