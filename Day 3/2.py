f = open('Day 3/input.txt')

totaal = 0

while True:
    line1 = f.readline()[:-1]
    line2 = f.readline()[:-1]
    line3 = f.readline()[:-1]

    if not line1:
        break

    for letter in set(line1):
        if line2.count(letter) >= 1 and line3.count(letter) >= 1:
            print(letter)
            if letter.isupper():
                totaal += ord(letter) - 64 + 26
            else:
                totaal += ord(letter) - 96

print(totaal)
