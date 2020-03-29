def min4(a, b, c, d):
    return min(min(min(a, b), c), d)


print(min4(4, 5, 6, 7))
print(min4(5, 4, 6, 7))
print(min4(5, 7, 4, 6))
