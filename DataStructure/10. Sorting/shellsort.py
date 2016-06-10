a = [2, 3, 4, 5, 2, 5, 31, 3, 14, 4235, 523, 253, 36, 63, 4]


def Shellsort(arr, h):
    for i in range(h, len(arr)):
        k = i - h
        key = arr[i]
        while k >= 0 and key < arr[k]:
            arr[k + h] = arr[k]
            k = k - h
        arr[k + h] = key
    return arr


print(Shellsort(Shellsort(Shellsort(a, 3), 2), 1))
