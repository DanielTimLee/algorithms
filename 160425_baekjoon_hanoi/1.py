n = input()

print(pow(2, n) - 1)


def hanoi(num, a, b):
    if num == 1:
        print
        "%d %d" % (a, b)
        return
    else:
        temp = 6 - a - b
        hanoi(num - 1, a, temp)
        print
        "%d %d" % (a, b)
        hanoi(num - 1, temp, b)


hanoi(n, 1, 3)
