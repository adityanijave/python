class test:
    k = 0
    def __init__(self,x,y):
        self.i = x
        self.j = y
        self.__class__.k += 1

    def sqr(self):
        self.i *= self.i
        self.j *= self.j

    def show(self):
        print(f"{self.i}\n{self.j}\n{self.__class__.k}")


print("++++++++++++++++++++++++")
ob1 = test(10,20)
ob1.sqr()
ob1.show()
print("++++++++++++++++++++++++")
ob2 = test(4,3)
ob2.sqr()
ob2.show()
print("++++++++++++++++++++++++")