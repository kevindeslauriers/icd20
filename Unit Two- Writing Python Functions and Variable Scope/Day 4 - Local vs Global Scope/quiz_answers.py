import math
car_type = "Hyundai"

#1a
print(len(car_type))

#1b
print(car_type[0:3])

#1c
print(car_type[len(car_type)-3:len(car_type)])

#2
def without_end(str):
    return str[1:len(str)-1]

#3
def volume_of_sphere(radius):
    return 4/3 * math.pi * radius**3

#4
def pythogorean(a,b):
    return math.sqrt(a**2 + b**2)


