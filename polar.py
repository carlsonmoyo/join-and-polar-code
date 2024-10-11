import math
def calculating_polar():
    A = float(input("enter y coordinate of a given point:")) #A is the given y control point
    B = float(input("enter x coordinate of a given point:")) # B is the given x control point
    D = float(input("enter distance between the points:"))
    C = float(input("enter direction between two points:"))
    yy = A + D*math.sin(C)
    xx = B + D*math.cos(C)
    print (yy)
    print (xx)
calculating_polar()
