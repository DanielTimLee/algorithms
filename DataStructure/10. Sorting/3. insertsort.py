a = [2, 3, 4, 5, 2, 5, 31, 3, 14, 4235, 523, 253, 36, 63, 4]
a.insert(0, -1)  # 어떤 수든 상관없는데 0보다 작아야함

length = len(a)

for start_index in range(2, length):
    temp = a[start_index]
    insert_index = start_index

    while a[insert_index - 1] > temp:
        a[insert_index] = a[insert_index - 1]
        insert_index = insert_index - 1

    a[insert_index] = temp

del a[0]
