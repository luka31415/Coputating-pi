import random
import pygame as pg

def GeneratePoint():
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    return [x, y]

def CheckCircle(point, r):
    x = point[0]
    y = point[1]

    if x**2 + y**2 > r**2:
        return False
    else:
        return True

def ChangeCoordinates(point):
    return [250 * (point[0] + 1), 250 * (point[1] + 1)]

def PrintPoint(point, screen):
    point = ChangeCoordinates(point)
    pg.draw.circle(screen, (255, 192, 203), point, 2)

def Main():
    pg.init()
    screen = pg.display.set_mode((500, 500))
    pg.display.set_caption("PI")

    points = []
    numOfPoints = 500000
    r = 1
    numPointsInCircle = 0

    for i in range(numOfPoints):
        points.append(GeneratePoint())

    for point in points:
        if CheckCircle(point, r):
            numPointsInCircle += 1

    pi = 4 * numPointsInCircle / numOfPoints

    print(pi)

    pg.draw.circle(screen, (0, 200, 0), (250, 250), 250)
    for point in points[0:(numOfPoints//100)]:
        PrintPoint(point, screen)
    pg.display.update()

if __name__ == '__main__':
    Main()
    while True:
        pass
