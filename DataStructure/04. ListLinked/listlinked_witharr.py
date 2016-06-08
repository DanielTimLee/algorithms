# 04. 리스트(링크드) 구조

class __ListLinked:
    class __Link:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    lists = []

    def __init__(self):
        self.numOfData = 0
        self.curPos = -1

    def CreateLink(self):
        data = input()
        self.lists.append(self.__Link(data))
        self.curPos += 1
        self.numOfData += 1
        if self.numOfData > 1:
            self.lists[self.curPos - 1].next = self.lists[self.curPos]
            self.lists[self.curPos].prev = self.lists[self.curPos - 1]

    def DeleteLink(self):
        data = input()
        for idx, _list in enumerate(self.lists):
            if data in _list.data:
                if idx == 0:
                    self.lists[idx + 1].prev = None
                elif idx != 0 and idx == (self.numOfData - 1):
                    self.lists[idx - 1].next = None
                else:
                    self.lists[idx - 1].next = self.lists[idx + 1]
                    self.lists[idx + 1].prev = self.lists[idx - 1]

                self.lists.pop(idx)
                self.curPos -= 1
                self.numOfData -= 1

    def Print(self):
        list = self.lists[0]
        while True:
            print(list.data)
            if list.next == None:
                break
            list = list.next


def ListLinked():
    list = __ListLinked()
    list.CreateLink()
    list.CreateLink()
    list.CreateLink()

    list.DeleteLink()


ListLinked()
