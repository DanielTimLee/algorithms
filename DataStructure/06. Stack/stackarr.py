import sys


class __stackArr:
    stk = []

    def __init__(self):
        self.topIndex = -1

    def SIsEmpty(self):
        if self.topIndex == -1:
            return True
        else:
            return False

    def SPush(self, data):
        print(data)
        self.topIndex += 1
        self.stk.append(data)

    def SPop(self):
        if self.SIsEmpty() == True:
            print("Stack Pop Error")
            sys.exit()

        print(self.stk.pop(self.topIndex))
        self.topIndex -= 1


def main():
    stack = __stackArr()
    stack.SPush(3)
    stack.SPush(2)
    stack.SPush(4)
    stack.SPush(5)
    stack.SPush(2)
    stack.SPush(1)
    stack.SPush(2)
    stack.SPush(3)
    print("")
    stack.SPop()
    stack.SPop()
    stack.SPop()
    stack.SPop()
    stack.SPop()
    stack.SPop()
    stack.SPop()
    stack.SPop()


main()
