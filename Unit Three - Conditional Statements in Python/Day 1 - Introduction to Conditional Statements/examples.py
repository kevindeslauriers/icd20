# Check if a number is positive.
number = int(input("Please enter a number: "))
if number > 0:
    print(f"{number} is positive")

if number <= 0:
    print(f"{number} is not positive")

# Determine if a person can vote (age 18 or older).
age = int(input("Please enter your age: "))

# if age >= 18:
#     eligable = ""
# if age < 18:
#     eligable = "not "

# print(f"You are eligable to {eligable}vote.")

if age >= 18:
    print("You are eligable to vote.")

if age < 18:
    print("You are not eligable to not")

# Check if a string is empty.
str = input("Please enter a String: ")
if len(str) == 0:
    print("The String is Empty")

if len(str) != 0:
    print("The String is not Empty")

# Write a function that returns the maximum/larger of two numbers.
def max_number(a, b):
    if a > b:
        return a

    return b

# use the function for testing
print(max_number(4,5))
print(max_number(14,5))


# Check if a user's input is equal to a secret password.
def password_checker(password, user_input):
    if password == user_input:
        return True
    
    return False

pwd = input("Password: ")
secret = "GJGHJGHKJGKJH"
print(password_checker(secret, pwd))

# def password_checker(password, user_input):
#     return password == user_input
        
# Write a function that checks if a number is within a specific range (lower-upper inclusive).

def range_checker(num, lower, upper):
    if lower <= num <= upper:
        return True
    
    return False

a = int(input("Please enter a number between 1 and 10: "))
if range_checker(a, 1, 10):
    print("Good you listen to instructions!!!")

if range_checker(a, 1, 10) == False:
    print("ARGHHH!!! I am not happy because you DON'T LISTEN!")

# Write a function that accepts a numberical grade and returns the Letter Grade
def grade_converter(grade):
    if grade >= 80:
        return "A"
    if grade >= 70:
        return "B"
    if grade >= 60:
        return "C"
    if grade >= 50:
        return "D"
    
    return "F"