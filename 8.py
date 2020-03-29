def my_xor(a, b):
    return (a and not b) or (b and not a)


def yesnoprint(x):
    if x is True:
        print(1)
    else:
        print(0)


yesnoprint(my_xor(0, 0))
yesnoprint(my_xor(0, 1))
yesnoprint(my_xor(1, 0))
