def min4(*args):
    res, *rest = args
    for x in rest:
        res = x if x < res else res
    return res


print(min4(4, 5, 6, 7))
print(min4(5, 4, 6, 7))
print(min4(5, 7, 4, 6))
