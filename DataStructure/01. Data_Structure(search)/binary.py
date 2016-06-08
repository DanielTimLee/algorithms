def binary(list):
    target = 23

    len(list)
    first = 0
    last = len(list) - 1

    while first <= last:
        mid = (first + last) // 2
        if target == list[mid]:
            return mid
        elif target < list[mid]:
            last = mid - 1
        elif target > list[mid]:
            first = mid + 1
    return False


list = [3, 4, 6, 7, 8, 9, 0, 0, 0, 8, 7, 6, 5, 4, 3, 32, 12, 13, 23, 3, 23, 1]
list.sort()
print(binary(list))
