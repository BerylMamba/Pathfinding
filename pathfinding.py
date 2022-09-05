boxWidth = 11
boxLength = 11

box = [
    list('###########'),
    list('#X        #'),
    list('#         #'),
    list('#         #'),
    list('#         #'),
    list('#         #'),
    list('#         #'),
    list('#      ####'),
    list('#      #  #'),
    list('#        X#'),
    list('###########'),
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

            if box[nextX][nextY] == '#':
                continue

            findPath.append(currentPath + [nextCoord])
            visitedCoords += [nextCoord]


print(shortestPath)
