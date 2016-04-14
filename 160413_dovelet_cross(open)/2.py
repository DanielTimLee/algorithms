l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l1.sort()
l2.sort()
if l1[1] < l2[0] or l2[1] < l1[0]:
    print("not cross")

else:
    if (l1[1] - l2[1]) * (l1[0] - l2[0]) > 0:
        print("cross")
    else:
        print("not cross")
