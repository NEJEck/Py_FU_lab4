def fastExp(b, n):
    def even(n):
        if n % 2 == 0:
            return 1
        return 0
    if n == 0:
        return 1
    if even(n):
        return fastExp(b, n/2) ** 2
    return b * fastExp(b, n-1)


print(fastExp(2, 1))
print(fastExp(2, 2))
print(fastExp(2, 3))
