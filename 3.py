from math import sqrt


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


print(toFixed(distance(0, 0, 1, 0) + distance(1, 0, 0, 1) + distance(0, 0, 0, 1), 6))
print(toFixed(distance(-2, -4, -3, -4) + distance(-2, -4, -1, 1) + distance(-3, -4, -1, 1), 6))

