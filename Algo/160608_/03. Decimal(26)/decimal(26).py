# 3.진수 계산기
decimal = 29
TWENTY_SIX = 26
hex = []
while True:
    hex.append(decimal % TWENTY_SIX)
    decimal = int(decimal / TWENTY_SIX)
    if (decimal == 0):
        break

print(hex[::-1])


# 진수 계산기 거꾸로
def twenty(i, j):
    return j * pow(TWENTY_SIX, i)


value = 0
for i, j in enumerate(hex):
    value += twenty(i, j)
    print(value)
