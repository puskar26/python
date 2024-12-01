import math

def circle(radius):
    area = math.pi * radius * radius
    circum = 2 * math.pi * radius
    return area, circum

Area, Circumference = circle(3)

print(round(Area,2), round(Circumference, 2))