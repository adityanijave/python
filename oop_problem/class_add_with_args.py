class sum :
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("values are stored")
    def add(self):
        print(f"The sum of the given values {self.x } and {self.y} is {self.x + self.y}.")

# objectname = classname()
op = sum(10,20)
op.add()