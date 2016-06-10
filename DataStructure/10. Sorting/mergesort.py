def mergeSort(x):
    if len(x) <= 1:
        return x

    m = len(x) // 2
    L = mergeSort(x[:m])
    R = mergeSort(x[m:])

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
mergeSort(a)
