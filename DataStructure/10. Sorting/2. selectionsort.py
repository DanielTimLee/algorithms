a = [2, 3, 4, 5, 2, 5, 31, 3, 14, 4235, 523, 253, 36, 63, 4]

length = len(a)
for i in range(length - 1):
    for j in range(i + 1, length - 1):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
