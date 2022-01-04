class A:
    def addition(self, x, y):
        self.x = x
        self.y = y
        print(f"addition is {self.x+self.y}")
# base class # parent class


class B(A):
    def sub(self, x, y):
        self.x = x
        self.y = y
        print(f"sub is {self.x-self.y}")
# derived class # child class


x = int(input("enter number : "))
y = int(input("enter number : "))
ob1 = B()
ob1.addition(x, y)
ob1.sub(x, y)
