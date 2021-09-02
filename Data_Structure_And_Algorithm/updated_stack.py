class stack:
    def __init__(self):
        self.top = -1
        self.arr = []
        self.max = 5
    def push(self,x):
        if self.top == self.max-1:
            print(f"stack is overflow!!!!!!!!")
        else:
            self.top += 1
            self.arr.insert(self.top,x)
            print(f"{x} pushed at {self.top}")
    def pop(self):
        if self.top == -1:
            print(f"Stack is underflow!!!!!!!")
        else:
            print(f"Poped item is {self.arr[self.top]}")
            self.top -= 1
    def show(self):
        if self.top == -1:
            print(f"stack is empty")
        else:
            print(f"stack item are : ")
            for i in range(self.top,-1,-1):
                print(self.arr[i])

st = stack()
st.push(0)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.pop()
st.pop()
st.show()
