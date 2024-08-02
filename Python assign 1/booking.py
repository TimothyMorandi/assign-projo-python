import math

def volCylinder(r,h):
    vol = math.pi*math.pwr(r,3)*h
    return(vol)
print(volCylinder(7,10))
