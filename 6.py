def IsPointInCircle(x, y, xc, yc, r):
    return "YES" if (x - xc) ** 2 + (y - yc) ** 2 <= r * r else "NO"


print(IsPointInCircle(0.5, 0.5, 0, 0, 1))
print(IsPointInCircle(0.5, 0.5, 1, 1, 0.1))
print(IsPointInCircle(0, 0, 1, 0, 1))
