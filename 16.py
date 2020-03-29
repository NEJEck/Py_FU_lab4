def gcd3(a, b):
    return a if b == 0 else gcd3(b, a % b)


def ReduceFraction(n, m):
    k = gcd3(n, m)
    return n // k, m // k


print(*ReduceFraction(12, 16))
print(*ReduceFraction(7, 9))
print(*ReduceFraction(10, 100))
