#part1
with open('day3\\input.txt', 'r') as file:
    score = 0
    for line in file:
        firstSack = set(line[:len(line)//2])
        secondSack = set(line[len(line)//2:])
        commonItem = list(firstSack & secondSack)[0]
        if commonItem.isupper(): score += ord(commonItem) - 38
        else: score += ord(commonItem) - 96
print(score)

#part2
score = 0
allLines = open('day3\\input.txt', 'r').read().splitlines()
first = allLines[0::3]
second = allLines[1::3]
third = allLines[2::3]
for x in range(len(first)):
    group = list(set.intersection(set(first[x]), set(second[x]), set(third[x])))[0]
    if group.isupper(): score += ord(group) - 38
    else: score += ord(group) - 96
print(score)
    



