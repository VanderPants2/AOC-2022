f = open('Day 3/input.txt')

totaal = 0

for x in f:
    string1 = x[0:int((len(x)/2-0.5))]
    string2 = x[int((len(x)/2-0.5)): len(x)-1]
    for letter in set(string1):
        if string2.count(letter) >= 1:
            print(letter)
            if letter.isupper():
                totaal += ord(letter) - 64 + 26
            else:
                totaal += ord(letter) - 96

print(totaal)
