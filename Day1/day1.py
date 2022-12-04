import heapq
import functools

inputFile = open('input1.txt', 'r')
lines = inputFile.readlines()
highest = 0
current = 0

#part1
for line in lines:
    if line == '\n' :
        if current > highest :
            highest = current
        current = 0
    else:
        current += int(line)

print(highest)

#part2
highest = 0
current = 0
list = []
for line in lines:
    if line == '\n' :
        list.append(current)
        current = 0
    else:
        current += int(line)
        
print(functools.reduce(lambda a, b: a+b, heapq.nlargest(3, list)))