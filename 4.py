def IsPointInSquare(x, y):
    bool1 = (-1 <= x <= 1)
    bool2 = (-1 <= y <= 1)
    return bool1 and bool2


def yesnoprint(x):
    if x is True:
        print("YES")
    else:
        print("NO")


yesnoprint(IsPointInSquare(0, 0))
yesnoprint(IsPointInSquare(3, -7))
yesnoprint(IsPointInSquare(0.5, 0.5))
