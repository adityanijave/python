def SpeedOFBoat(d, t1, t2):
    ds = d / t1
    us = d / t2
    r = ds + us
    fr = r / 2
    print(int(fr))


d = int(input())
t1 = int(input())
t2 = int(input())
SpeedOFBoat(d, t1, t2)
