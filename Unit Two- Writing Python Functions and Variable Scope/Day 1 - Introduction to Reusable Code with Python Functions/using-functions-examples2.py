# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return length * width
    else:
        return "Invalid input. Please provide numeric values for length and width."

# Function to check if a string contains a specific substring
def contains_substring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return substring in string
    else:
        return "Invalid input. Please provide two strings."

# Function to calculate the average of three floats
def average_of_three_floats(num1, num2, num3):
    if all(isinstance(x, float) for x in [num1, num2, num3]):
        return (num1 + num2 + num3) / 3.0
    else:
        return "Invalid input. Please provide three floating-point numbers."

# Function to concatenate two strings
def concatenate_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        return str1 + str2

# Function to calculate the volume of a cube
def volume_of_cube(side_length):
    if isinstance(side_length, (int, float)):
        return side_length ** 3

# Function to check if a number is positive, negative, or zero
def check_number_status(number):
    if isinstance(number, (int, float)):
        if number > 0:
            return "Positive"
        elif number < 0:
            return "Negative"
        else:
            return "Zero"

# Function to calculate the circumference of a circle
def circumference_of_circle(radius):
    if isinstance(radius, (int, float)):
        return 2 * 3.141592653589793 * radius

# Function to count the number of occurrences of a character in a string
def count_char_occurrences(string, char):
    if isinstance(string, str) and isinstance(char, str) and len(char) == 1:
        return string.count(char)

# Function to calculate the percentage of a number
def calculate_percentage(number, percentage):
    if isinstance(number, (int, float)) and isinstance(percentage, (int, float)):
        return (percentage / 100) * number

# Function to find the absolute difference between two numbers
def absolute_difference(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        return abs(num1 - num2)

# Function to capitalize the first letter of a string
def capitalize_first_letter(string):
    if isinstance(string, str):
        return string.capitalize()

# Function to calculate the square of a number
def square(number):
    if isinstance(number, (int, float)):
        return number ** 2

# Function to find the maximum of two numbers
def max_of_two(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        if num1 > num2:
            return num1
        else:
            return num2

# Function to calculate the square root of a number
def square_root(number):
    if isinstance(number, (int, float)) and number >= 0:
        return number ** 0.5

# Function to find the length of a string
def length(input_data):
    if isinstance(input_data, str):
        return len(input_data)
    
##########################################################################


# Examples of calling the functions:

# Calculate the area of a rectangle
rectangle_area = area_of_rectangle(5.0, 3.0)
print("Area of the rectangle: ", rectangle_area)

# Check if a string contains a specific substring
contains = contains_substring("Hello, World!", "World")
print("String contains 'World': ", contains)

# Calculate the average of three floats
avg_three_floats = average_of_three_floats(4.5, 2.7, 8.3)
print("Average of three floats: ", avg_three_floats)

# Concatenate two strings
concatenated_string = concatenate_strings("Hello, ", "World!")
print("Concatenated string: ", concatenated_string)

# Calculate the volume of a cube
cube_volume = volume_of_cube(3.0)
print("Volume of the cube: ", cube_volume)

# Check if a number is positive, negative, or zero
number_status = check_number_status(-5)
print("Number status: ", number_status)

# Calculate the circumference of a circle
circle_circumference = circumference_of_circle(4.0)
print("Circumference of the circle: ", circle_circumference)

# Count the number of occurrences of a character in a string
char_count = count_char_occurrences("programming", "r")
print("Number of 'r' in 'programming': ", char_count)

# Calculate the percentage of a number
percentage_result = calculate_percentage(80, 25)
print("25% of 80: ", percentage_result)

# Find the absolute difference between two numbers
abs_difference = absolute_difference(7.5, 3.2)
print("Absolute difference between 7.5 and 3.2: ", abs_difference)

# Capitalize the first letter of a string
capitalized_string = capitalize_first_letter("chatgpt")
print("Capitalized string: ", capitalized_string)

# Calculate the square of a number
number_squared = square(4)
print("Square of 4: ", number_squared)

# Find the maximum of two numbers
maximum_number = max_of_two(8.7, 5.2)
print("Maximum of 8.7 and 5.2: ", maximum_number)

# Calculate the square root of a number
sqrt_result = square_root(16.0)
print("Square root of 16: ", sqrt_result)

# Find the length of a string
string_length = length("Python is fun!")
print("Length of the string: ", string_length)


