c = int(input())
d = list(map(int, input().split()))
n = int(input())
l = list()
v = 0
for i in range(n):
    l.append(int(input()))
    if float(sum(d)) / 2 > l[i]:
        d[0] = l[i]
    v += abs(d[0] - l[i])
else:
    v += abs(d[1] - l[i])
    d[1] = l[i]
print(v)
