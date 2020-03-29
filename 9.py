from math import sqrt


def MinDivisor(n):
    i = 2
    while n % i != 0:
        if i >= sqrt(n):
            print(n)
            return
        i += 1
    print(i)


MinDivisor(4)
MinDivisor(5)
MinDivisor(3)
