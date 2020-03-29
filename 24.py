def sqr():
    n = int(input())
    if n != 0:
        sqr()
        if (n ** (1 / 2)).is_integer():
            global t
            t = 0
            print(n, end=' ')


t = 1
sqr()
if t:
    print(0)