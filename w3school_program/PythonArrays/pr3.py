index = 1


def Cars(carappend=""):
    cars = ["TATA", "BMW", "AVANTI"]

    def callingLoop():
        global index
        for i in cars:
            print(f"At no {index} , the car name is {i}")
            index += 1

    if len(carappend) != 0 and carappend not in cars:
        cars.append(carappend)
        callingLoop()
    else:
        callingLoop()


Cars("honda")
