import sys


class __StkLink:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def main():
    global head
    head = None

    Push(3)
    Push(2)
    Push(4)
    Push(1)
    Push(4)
    Push(1)
    Push(3)
    print("")
    Pop()
    Pop()
    Pop()
    Pop()
    Pop()
    Pop()
    Pop()
    Pop()


def Push(data):
    global head
    newNode = __StkLink(data, head)
    head = newNode


def Pop():
    global head
    if SIsEmpty() == True:
        print("error")
        sys.exit()
    print(head.data)
    NewHead = head.next
    del head
    head = NewHead


def SIsEmpty():
    global head
    if head == None:
        return True
    else:
        return False


main()
