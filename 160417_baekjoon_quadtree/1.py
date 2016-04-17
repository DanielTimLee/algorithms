from math import log

n = int(input())
arr = [[], [], [], [], [], [], []]
num = int(log(n, 2))
for a in range(n):
    arr[num].append(list(map(int, input())))

for i in range(num - 1, -1, -1):
    for j in range(2 ** (i)):
        arr[i].append([])
        for k in range(2 ** (i)):
            arr[i][j].append((lambda a, b, c, d: a if a == b == c == d else [a, b, c, d])(arr[i + 1][j * 2][k * 2],
                                                                                          arr[i + 1][j * 2][k * 2 + 1],
                                                                                          arr[i + 1][j * 2 + 1][k * 2],
                                                                                          arr[i + 1][j * 2 + 1][
                                                                                              k * 2 + 1]))

ans = str(arr[0]).replace(", ", "")
ans = ans[2:-2].replace("[", "(")
ans = ans.replace("]", ")")
print(ans)
