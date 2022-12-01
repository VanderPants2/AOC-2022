f = open('Day 1/input.txt')

big = 0
sum = 0

for x in f:
    if x != '\n':
        sum += int(x[:-1])
    else:
        big = sum if sum > big else big
        sum = 0

print(big)
