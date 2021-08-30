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
bulb_1 = bulb
bulb_1.turnOn(bulb_1)
bulb_1.status_of_bulb()
#














































