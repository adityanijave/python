class bulb:
    def __init__(self):
        self.isOn = False

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def status_of_bulb(self):
        if self.isOn == True:
            print("on")
        else:
            print("off")


# objectname = classname()
bulb_1 = bulb()

bulb_1.turnOn()
bulb_1.status_of_bulb()
bulb_1.turnOff()
bulb_1.status_of_bulb()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

bulb_2 = bulb()
bulb_2.status_of_bulb()
bulb_2.turnOn()
bulb_2.status_of_bulb()
bulb_2.turnOff()
bulb_2.status_of_bulb()











































