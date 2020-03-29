def IsPointInCircle(x, y):
    xc = -1
    yc = 1
    r = 2
    return (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r


def IsPointInsideCircle(x, y):
    xc = -1
    yc = 1
    r = 2
    return (x - xc) * (x - xc) + (y - yc) * (y - yc) < r * r


def IsPointInArea(x, y):
    left_line_right = (x + y >= 0)
    right_line_left = (2 * x - y + 2 <= 0)
    left_line_left = (x + y <= 0)
    right_line_right = (2 * x - y + 2 >= 0)
    in_circ_area = IsPointInCircle(x, y) and left_line_right and right_line_left
    in_bottom = (not (IsPointInsideCircle(x, y)) and left_line_left and right_line_right)
    return in_circ_area or in_bottom


def yesnoprint(x):
    if x is True:
        print("YES")
    else:
        print("NO")


yesnoprint(IsPointInArea(0, -5))
yesnoprint(IsPointInArea(-4, -4))
yesnoprint(IsPointInArea(4, 4))
yesnoprint(IsPointInArea(-4, -2))
