flag = input()
a = input(), input()
a = list(a)
a.sort()
if (flag == '1'):
    if (a[0] == a[1]):
        print - 1
    else:
        print("%.2f" % (float(a[0]) ** 2 / (float(int(a[1]) - int(a[0]))) + int(a[0])))
else:

    c = 600 / float(a[0])
    d = 600 / float(a[1])
    p = 10 / (c + d)
    q = (10 / c) - p

    print("%.2f" % (((10 - (q * d - ((10 - p * d)) % 10)) / (c + d)) * 60))
