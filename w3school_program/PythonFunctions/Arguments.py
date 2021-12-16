id = 1


def studentName(first="no name enter"):
    global id
    print(f"The name of student is {first} and id is {id}")
    id += 1


studentName("ruhi")
studentName("adi")
studentName("adi_ruhi")
studentName()
