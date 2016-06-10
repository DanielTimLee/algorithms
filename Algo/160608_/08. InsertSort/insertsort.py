import random

b = []
for i in range(15):
    b.append(random.randint(1, 1000))


def insertsort(arr):
    arr.insert(0, -1)

    for start_idx in range(2, len(arr)):
        key = arr[start_idx]
        insert_idx = start_idx

        while arr[insert_idx - 1] > key:
            arr[insert_idx] = arr[insert_idx - 1]
            insert_idx = insert_idx - 1
        arr[insert_idx] = key

    arr.pop(0)
    return arr


print(insertsort(b))
