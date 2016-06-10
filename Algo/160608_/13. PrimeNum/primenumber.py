# 13. 소수 구하기
prime = [2, 3];
for i in range(4, 200):
    c = 0
    for s in prime:
        if i % s == 0:
            c = 1
            break
    if c == 1:
        continue

    prime.append(i)
    a = '{0} is prime'.format(i)
    print(a)
