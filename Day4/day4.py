#part1
file = open('day4\\input.txt', 'r').read().splitlines()
score = 0
for line in file:
    pairs = line.split(",")
    first = pairs[0].split("-")
    second = pairs[1].split("-")
    firstRange = set(range(int(first[0]), int(first[1])+1))
    secondRange = set(range(int(second[0]), int(second[1])+1))
    overlap = firstRange.intersection(secondRange)
    if len(overlap) == len(firstRange) or len(overlap) == len(secondRange):
        score += 1
print(score)


#part2
file = open('day4\\input.txt', 'r').read().splitlines()
score = 0
for line in file:
    pairs = line.split(",")
    first = pairs[0].split("-")
    second = pairs[1].split("-")
    firstRange = set(range(int(first[0]), int(first[1])+1))
    secondRange = set(range(int(second[0]), int(second[1])+1))
    overlap = firstRange.intersection(secondRange)
    if len(overlap) is not 0:
        score += 1
print(score)
