import random

b = []
for i in range(15):
    b.append(random.randint(1, 1000))


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = []
    equal = []
    more = []

    for i in arr:
        if i == pivot:
            equal.append(i)
        elif i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)

    return quicksort(less) + equal + quicksort(more)


print(quicksort(b))
