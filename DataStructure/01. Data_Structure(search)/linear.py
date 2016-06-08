def linear(list):
    target = 23
    for idx, _list in enumerate(list):
        if target == _list:
            print(idx)
    return


list = [3, 4, 6, 7, 8, 9, 0, 0, 0, 8, 7, 6, 5, 4, 3, 32, 12, 13, 23, 3, 23, 1]

linear(list)
