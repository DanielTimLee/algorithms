# 4. 최소공배수 / 최대공약수 구하기
def gcd(a, b):
    c = [a, b]
    c.sort()
    d = generateDivisor(c[0])
    gcmDivisor = []
    for i in d:
        c[1] % i == 0
        gcmDivisor.append(i)

    return gcmDivisor[-1]


def generateDivisor(a):
    divisor = []
    for i in range(a):
        if (a % (i + 1) == 0):
            divisor.append(i + 1)
    return divisor


gcd(7, 2)
gcd(72, 192)


def lcm(a, b):
    print(int(a * b / gcd(a, b)))


lcm(7, 2)
lcm(72, 192)
