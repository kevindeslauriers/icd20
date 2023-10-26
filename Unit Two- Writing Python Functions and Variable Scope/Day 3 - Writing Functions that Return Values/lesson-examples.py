import math

# arguments:
# function name:
# what does it return: 
def calculate_cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def convert_temperature(degrees, scale):
    if scale.lower() == 'celsius':
        fahrenheit = (degrees * 9/5) + 32
        return fahrenheit
    elif scale.lower() == 'fahrenheit':
        celsius = (degrees - 32) * 5/9
        return celsius
    else:
        return None

def larger_string(string_a, string_b):
    len_a = len(string_a)           # len(str) returns the # of characters in the String
    len_b = len(string_b)

    if len_a > len_b:
        return string_a
    elif len_b > len_a:
        return string_b
    else:
        return "Same"
    
def first_two(str):
    return str[0:2]


# once we get to a line that returns a value the function is over
def test_return_twice():
    a = 7
    return a
    a = 8   # never happens -> unreachable code
    return a

# r = 10
# h = 5
# print(f"The volume of a cylinder with height {h} and radius {r} is {calculate_cylinder_volume(r,h):.2f}")

print(test_return_twice())

print(first_two("Steve"))


