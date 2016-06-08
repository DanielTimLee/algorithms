from math import log

n = input()
arr = []
num = int(log(n, 3))
for a in range(num):
    arr.append(map(int, raw_input()))


def create(key):
    global l2st
    l2st = []
    for i in range(n / 3 - 1, -1 - 1):
        for j in range(n / 3 - 1, -1 - 1):
            l2st.append(arr[i][j])


global a, b, c


def check(l2st):
    if len(set(l2st)) > 1:
        # 9일때 비교
        if len(l2st) == 9:
            for val in l2st:
                if val == 1:
                    a += 1
                elif val == 0:
                    b += 1
                elif val == -1:
                    c += 1
        else:
            create(key)
            check(l2st)

    else:
        val = set(l2st).pop()
        if val == 1:
            a += 1
        elif val == 0:
            b += 1
        elif val == -1:
            c += 1



            #     for j in range(2 ** (i)):
            #         arr[i].append([])
            #         for k in range(2 ** (i)):
            #             arr[i][j].append((lambda a, b, c, d: a if
            #             (type(arr[i+1][j*2][k*2]))==int and a == b == c == d
            #             else [a, b, c, d])(arr[i + 1][j * 2][k * 2],
            #                                arr[i + 1][j * 2][k * 2 + 1],
            #                                arr[i + 1][j * 2 + 1][k * 2],
            #                                arr[i + 1][j * 2 + 1][k * 2 + 1]))
            #
            # ans = str(arr[0]).replace(", ", "")
            # ans = ans[2:-2].replace("[", "(")
            # ans = ans.replace("]", ")")
            # print(ans)
            # for i in range(num - 1, -1, -1):
