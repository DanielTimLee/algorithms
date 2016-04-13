a, b = map(int, input().split())
p, q = map(lambda x: int(x ** 0.5), (a - 1, b))
print((b - a + 1) - (q - p))
