def gcd3(a, b):
    return a if b == 0 else gcd3(b, a % b)


print(gcd3(1, 1))
print(gcd3(2, 1))
print(gcd3(2, 2))
