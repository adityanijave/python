class MyNumbers:
    def __iter__(self):
      self.a = 1
      return self

    def __next__(self):
      x = self.a
      self.a += 1
      return x


myClass = MyNumbers()
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
