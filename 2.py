from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


print(distance(0, 0, 1, 1))
print(distance(0, 0, 1, 0))
print(distance(3, -2, -1, 7))
