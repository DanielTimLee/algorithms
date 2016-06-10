import random

b = []
for i in range(14):
    b.append(random.randint(1, 1000))


def radixsort(arr, time):
    if type(arr[0]) == list:
        new_arr = []
        for idx in range(10):
            try:
                for i in range(100):
                    new_arr.append(arr[idx].pop(0))
            except:
                IndexError
        print(new_arr)
        arr = new_arr

    sortarr = [[], [], [], [], [], [], [], [], [], []]

    for idx, i in enumerate(arr):
        k = str(i % (10 ** time))
        sortarr[int(k[0])].append(arr[idx])
    return sortarr


ary = radixsort(b, 1)
print(ary)

c = radixsort(ary, 2)
print(c)

d = radixsort(c, 3)
print(d)
