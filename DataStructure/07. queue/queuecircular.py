class __queueCircular:
    QUE_LEN = 4
    arr = [None] * QUE_LEN

    def __init__(self):
        self.front = 0
        self.rear = 0

    def QIsEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def NextPosIdx(self):
        if self.rear == (self.QUE_LEN - 1):
            return 0
        else:
            return self.rear + 1

    def QIsFull(self):
        if self.arr[-1] != None and self.arr[1] != None:
            return True
        else:
            return False

    def Enqueue(self, data):
        if self.NextPosIdx(self) == self.front:
            print("Error")
            return
        self.rear += 1
        self.data = data

    def Dequeue(self, data):
        self.front += 1
        del self.arr[self.front]


def main():
    queue = __queueCircular()
    queue.Enqueue(2)
    queue.Enqueue(6)
    queue.Enqueue(1)
    queue.Enqueue(4)
    queue.Enqueue(4)

    queue.Dequeue()
    queue.Dequeue()
    queue.Dequeue()
    queue.Dequeue()
    queue.Dequeue()
