def IsPointInSquare(x, y):
    x_l = -1
    x_r = 1
    y_b = -1
    y_t = 1
    x_in_sq = (x >= x_l) and (x <= x_r)
    y_in_sq = (y >= y_b) and (y <= y_t)
    sum_xy = abs(x) + abs(y) <= 1
    return x_in_sq and y_in_sq and sum_xy


def yesnoprint(x):
    if x is True:
        print("YES")
    else:
        print("NO")


yesnoprint(IsPointInSquare(0, 0))
yesnoprint(IsPointInSquare(1, 1))
yesnoprint(IsPointInSquare(-1, -1))
