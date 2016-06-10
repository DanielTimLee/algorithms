def hanoi(num, a, b):
    if num == 1:
        a = "{0} {1}".format(a, b)
        print(a)
        return

    else:
        temp = 6 - a - b
        hanoi(num - 1, a, temp)
        a = "{0} {1}".format(a, b)
        print(a)
        hanoi(num - 1, temp, b)
