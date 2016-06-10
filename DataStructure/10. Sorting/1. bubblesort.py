a = [2, 3, 4, 5, 2, 5, 31, 3, 14, 4235, 523, 253, 36, 63, 4]

length = len(a)
for i in range(length - 1):
    for j in range(length - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
