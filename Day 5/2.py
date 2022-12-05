f = open('Day 5/input.txt')

test_platform = [
    ['z', 'n'],
    ['m', 'c', 'd'],
    ['p']
]

platform = [
    ['h', 'c', 'r',],
    ['b', 'j', 'h', 'l', 's', 'f',],
    ['r', 'm', 'd', 'h', 'j', 't', 'q',],
    ['s', 'g', 'r', 'h', 'z', 'b', 'j',],
    ['r', 'p', 'f', 'z', 't', 'd', 'c', 'b',],
    ['t', 'h', 'c', 'g',],
    ['s', 'n', 'v', 'z', 'b', 'p', 'w', 'l',],
    ['r', 'j', 'q', 'g', 'c',],
    ['l', 'd', 't', 'r', 'h', 'p', 'f', 's',],
]

for x in f:
    x = x[:-1].split(' ')
    x.pop(0)
    x.pop(1)
    x.pop(2)
    x = [int(y)-1 for y in x]
    for y in range(0, x[0]+1):
        platform[x[2]].append(platform[x[1]][0-x[0]+y-1])
    for y in range(0, x[0]+1):
        platform[x[1]].pop()

top = ''

for stack in platform:
    top += stack[-1]

print(top.upper())
