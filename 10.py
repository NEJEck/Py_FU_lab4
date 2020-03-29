from math import sqrt


def is_prime1(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1


def yesnoprint(x):
    if x is True:
        print("YES")
    else:
        print("NO")


yesnoprint(is_prime1(2))
yesnoprint(is_prime1(4))
yesnoprint(is_prime1(3))
