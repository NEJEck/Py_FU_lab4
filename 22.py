def printFourSquares(a):
    i = 0
    while i * i <= a:
        j = i
        while j * j <= a:
            k = j
            while k * k <= a:
                l = k
                while l * l <= a:
                    if i * i + j * j + k * k + l * l == a:
                        # printing the numbers
                        print("{} = {}*{} + {}*{} +".
                              format(a, i, i, j, j), end=" ")
                        print("{}*{} + {}*{}".
                              format(k, k, l, l), end="\n")
                    l = l + 1
                k = k + 1
            j = j + 1
        i = i + 1


printFourSquares(1)
printFourSquares(2)
printFourSquares(3)
printFourSquares(4)
