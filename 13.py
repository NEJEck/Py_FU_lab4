def sum(a, b):
    return sum(a + 1, b - 1) if b else a


print(sum(2, 2))
print(sum(123, 456))
print(sum(179, 0))
