# 03. 리스트(배열) 구조
class __ListArr:
    '''
    배열 생성, 삭제, 출력 등 기능 수행.
    :var numOfData
    :var curPos
    '''
    arr = list()

    def __init__(self):
        self.numOfData = 0
        self.curPos = -1

    def Insert(self, data):
        self.arr.append(data)
        self.numOfData += 1

    def Delete(self, data):
        self.First()

        while self.arr[self.curPos]:
            if self.arr[self.curPos] == data:
                self.arr.pop(self.curPos)
                self.numOfData -= 1
                self.curPos -= 1
            if self.Next() == False:
                break

    def Count(self):
        print(self.numOfData)

    def First(self):
        self.curPos = 0

    def Next(self):
        if (self.curPos + 1 >= self.numOfData):
            return False
        self.curPos += 1

    def Print(self):
        self.First()

        while self.arr[self.curPos]:
            print(self.arr[self.curPos])
            if self.Next() == False:
                break


def ListArr():
    list = __ListArr()

    list.Insert(1)
    list.Insert(1)
    list.Insert(2)
    list.Insert(2)
    list.Insert(3)

    list.Count()
    list.Print()
    list.Delete(2)
    list.Print()


ListArr()
