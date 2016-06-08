# 6. 버블정렬
ran_num = [7, 1, 7, 64, 9, 3, 7, 5, 43, 6, 67, 67, 4756, 4567, 32, 2, 5, 2, 6, 54, 4234, 1]


def bubblesort(arr):
    length = len(arr) - 1
    for i in range(length):
        for j in range(length - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


bubblesort(ran_num)
