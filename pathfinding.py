from tracemalloc import start

boxWidth = 11
boxLength = 11

box = [
    list('############'),
    list('#X         #'),
    list('#          #'),
    list('#          #'),
    list('#          #'),
    list('#          #'),
    list('#          #'),
    list('#          #'),
    list('#       ####'),
    list('#       #  #'),
    list('#         Y#'),
    list('############'),
]


def nextMoves(x, y):
    return {
        'left': [x-1, y],
        'right': [x+1, y],
        'up': [x, y-1],
        'down': [x, y+1],
    }.values()


def shortestPath(box, startCoord, endCoord):
    findPath = [[startCoord]]
    visitedCoords = [startCoord]

    while findPath != []:
        currentPath = findPath.pop(0)
        currentCoord = currentPath[-1]

        currentX, currentY = currentCoord

        if currentCoord == endCoord:
            return currentPath

        for nextCoord in nextMoves(currentX, currentY):
            nextX, nextY = nextCoord

            if nextX < 0 or nextX >= boxWidth:
                continue

            if nextY < 0 or nextY >= boxLength:
                continue

            if nextCoord in visitedCoords:
                continue

            if box[nextY][nextX] == '#':
                continue

            findPath.append(currentPath + [nextCoord])
            visitedCoords += [nextCoord]


path = shortestPath(box, [1, 1], [10, 10])

for coords in path:
    x, y = coords
    box[y][x] = '.'

    for row in box:
        print(''.join(row))
