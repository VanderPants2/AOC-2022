f = open('Day 6/input.txt')

letter_list = list(f.readline())
four_letter_list = []

for i in range(0, len(letter_list)):
    if len(four_letter_list) < 14:
        four_letter_list.append(letter_list[i])
    elif len(set(four_letter_list)) == len(four_letter_list):
        end = i
        break
    else:
        four_letter_list.pop(0)
        four_letter_list.append(letter_list[i])


print(end)
