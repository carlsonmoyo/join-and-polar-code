import math
def calculating_join():
    z1 = float(input("enter coordinate value of y:"))
    z2 = float(input("enter coordinate value of y1:"))
    n = z2 - z1
    print (n)
    v1 = float(input("enter coordinate value of x:"))
    v2 = float(input("enter coordinate value of x1:"))
    m = v2 - v1
    print (m)
    distance = math.sqrt((n ** 2) + (m ** 2))
    print (distance)
    direction = math.degrees(math.atan(n / m))
    print (direction)
    if n > 0 and m > 0:  # first quadrant
        print(direction)
    elif n > 0 and m < 0:  # second quadrant
        print(180 + direction)
    elif n < 0 and m < 0:
        print(direction + 180)  # third quadrant
    else:
        print(360 + direction)  # forth quadrant.
calculating_join()
