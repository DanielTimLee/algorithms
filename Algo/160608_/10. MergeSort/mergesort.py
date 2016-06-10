def mergesort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    L = mergesort(arr[:m])
    R = mergesort(arr[m:])

    result = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1

    result += L[i:]
    result += R[j:]

    return result


a = [21, 3, 234, 5, 12, 25, 31, 3, 14, 4235, 523, 253, 36, 63, 4]
print(mergesort(a))
