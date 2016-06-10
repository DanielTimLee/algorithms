class __treeBinary:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Print(self):
        print(self.data)

    def GetLeft(self):
        return self.left

    def GetRight(self):
        return self.right

    def Conn(self, left=None, right=None):
        self.left = left
        self.right = right


def main():
    global head

    t1 = __treeBinary(1)
    t2 = __treeBinary(2)
    t3 = __treeBinary(3)
    t4 = __treeBinary(4)

    t1.Conn(t2, t3)
    t2.Conn(t4)

    pass


main()
