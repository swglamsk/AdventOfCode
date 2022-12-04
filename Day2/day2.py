letters = "ABCXYZ"
numbers = "123123"

def round(enemy, player):
    if enemy == player:
        return player+3
    if enemy == 1 and player == 3:
        return player
    if enemy == 2 and player == 1:
        return player
    if enemy == 3 and player == 2:
        return player
    return player+6

def round2(enemy, player):
    match enemy, player:
        case 1, 1:
            return 3
        case 1, 2:
            return 4
        case 1, 3:
            return 8
        case 2, 1:
            return 1
        case 2, 2:
            return 5
        case 2, 3:
            return 9
        case 3, 1:
            return 2
        case 3, 2:
            return 6
        case 3, 3:
            return 7

#part1
with open('day2\\input.txt', 'r') as file:
    totalScore = 0
    for line in file:
        transTable = line.maketrans(letters, numbers)
        values = line.translate(transTable).split(" ")
        totalScore += round(int(values[0]), int(values[1]))
    print(totalScore)

#part2
with open('day2\\input.txt', 'r') as file:
    totalScore = 0
    for line in file:
        transTable = line.maketrans(letters, numbers)
        values = line.translate(transTable).split(" ")
        totalScore += round2(int(values[0]), int(values[1]))
    print(totalScore)
