class __Link:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next


def Add():
    global head, tail
    while True:
        data = input()

        if int(data) < 1:
            break

        newNode = __Link(data)

        if head == None:
            head = newNode

        else:
            tail.next = newNode

        tail = newNode


def Print():
    global head, tail
    cur = head

    while cur == None:
        print(cur.data)
        cur = cur.next


def DeleteAll():
    global head, tail

    if head == None:
        return

    else:
        delNode = head
        delNextNode = head.next

        del delNode

        while delNextNode != None:
            delNode = delNextNode
            delNextNode = delNextNode.next
            del delNode


def ListLinked():
    global head, tail
    head = None
    tail = None
    Add()
    Print()
    DeleteAll()


ListLinked()
