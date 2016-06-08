a, b = map(int, input().split())
c, d = map(int, input().split())
p = (a if a < b else b)
q = (a if a > b else b)

if (p < c < q) ^ (p < d < q):
    print("cross")
else:
    print("not cross")
