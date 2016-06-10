import random

a = []

for i in range(10):
    a.append(random.randint(1, 1000))


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    less = []
    equal = []
    more = []

    for num in arr:
        if num == pivot:
            equal.append(num)
        elif num < pivot:
            less.append(num)
        elif num > pivot:
            more.append(num)

    return quicksort(less) + equal + quicksort(more)


arc = quicksort(a)
print(arc)
