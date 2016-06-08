a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
if (a[0] < b[0] < a[1]) ^ (a[0] < b[1] < a[1]):
    print("cross")
else:
    print("not cross")
