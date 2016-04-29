n = input()
a = []

for i in range(n):
    a.append(raw_input())

for j in range(1, n):
    for i in range(len(a[0])):
        if a[0][i] != a[j][i]:
            a[0] = a[0][:i] + '?' + a[0][i + 1:]
print
a[0]
