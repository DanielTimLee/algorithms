# 7. 선택 정렬
ran_num = [7, 4, 7, 64, 9, 3, 7, 5, 43, 6, 67, 67, 4756, 4567, 32, 2, 5, 2, 6, 54, 4234, 1]


def selectionsort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


selectionsort(ran_num)
print(ran_num)
