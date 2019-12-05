import math

class Wire:

    def __init__(self):
        self.coordsByX = {}
        self.coordsByY = {}
        self.coords = []
        self.addCoord(Coordinate(0, 0))

    def parse(self, instructions):
        cursorX = 0
        cursorY = 0
        for i in instructions:
            direction = i[0]
            amount = int(i[1:len(i)])
            if direction == 'L':
                # Left
                deltaX = -1
                deltaY = 0
            elif direction == 'R':
                # Right
                deltaX = 1
                deltaY = 0
            elif direction == 'U':
                # Up
                deltaX = 0
                deltaY = 1
            elif direction == 'D':
                # Down
                deltaX = 0
                deltaY = -1
            for step in range(0, amount):
                cursorX += deltaX
                cursorY += deltaY
                coord = Coordinate(cursorX, cursorY)
                self.addCoord(coord)

    def addCoord(self, coord):
        self.coords.append(coord)
        if coord.x not in self.coordsByX.keys():
            self.coordsByX[coord.x] = []
        if coord.y not in self.coordsByY.keys():
            self.coordsByY[coord.y] = []
        self.coordsByX[coord.x].append(coord)
        self.coordsByY[coord.y].append(coord)

    def findIntersections(self, otherWire):
        intersections = []
        # Perform set intersection
        commonX = self.coordsByX.keys() & otherWire.coordsByX.keys()
        for x in commonX:
            for c1 in self.coordsByX[x]:
                for c2 in otherWire.coordsByX[x]:
                    if c1.y == c2.y:
                        if not (c1.x == 0 and c1.y == 0):
                            intersections.append(c1)
                            # print(c1, '\t', c1.manhattan())
        return intersections

    def distanceToCoord(self, coord):
        dist = 0
        for c in self.coords:
            if c == coord:
                return dist
            dist += 1


class Coordinate:
    x = 0
    y = 0

    def __init__(self, xPart, yPart):
        self.x = xPart
        self.y = yPart

    def __str__(self):
        return str(self.x) + ",\t" + str(self.y)

    def __eq__(self, other):
        return isinstance(other, Coordinate) and other.x == self.x and other.y == self.y

    def manhattan(self):
        return abs(self.x) + abs(self.y)


def star1():
    print('Star 1')
    w1 = Wire()
    w2 = Wire()
    with open("puzzles/day3.txt", "r") as f:
        instructionString = f.readline()
        instructions = instructionString.split(',')
        w1.parse(instructions)
        instructionString = f.readline()
        instructions = instructionString.split(',')
        w2.parse(instructions)

        # Get the intersection points (list of Coordinate)
        intPoints = w1.findIntersections(w2)
        print("********")
        print(min(wi.manhattan() for wi in intPoints))
        print("********")



def star2():
    print('Star 2')
    w1 = Wire()
    w2 = Wire()
    with open("puzzles/day3.txt", "r") as f:
        instructionString = f.readline()
        instructions = instructionString.split(',')
        w1.parse(instructions)
        instructionString = f.readline()
        instructions = instructionString.split(',')
        w2.parse(instructions)

        # Get the intersection points (list of Coordinate)
        intPoints = w1.findIntersections(w2)
        print("********")
        print(min((w1.distanceToCoord(wi) + w2.distanceToCoord(wi)) for wi in intPoints))
        print("********")