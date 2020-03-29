def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(power(2, 1))
print(power(2, 2))
print(power(2, 3))
