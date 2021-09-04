class test:
    s = "this is class variable"
    @classmethod
    def show(cls):
        print(cls.s)
ss = test()
ss.show()