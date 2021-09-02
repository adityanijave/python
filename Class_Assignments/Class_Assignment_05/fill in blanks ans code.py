class student :
    def __init__(self,name):
        self.name = name

    def sayHi(self):
        print(f"Hi from {self.name}")
s1 = student("ruhi")
s1.sayHi()