number_grade = 76

# These are all SEPERATE If Statements so they each run separetly
# if number_grade >= 80:
#     print("A")
# if number_grade >= 70:
#     print("B")
# if number_grade >= 60:
#     print("C")
# if number_grade >= 50:
#     print("D")
# if number_grade < 50:
#     print("F")

# prints B C D on seperate lines because 3 conditions were true

# The following code has 5 seperate if statements - evaluates 5 conditions
# if number_grade >= 80:
#     print("A")
# if 70 <= number_grade < 80:
#     print("B")
# if 60 <= number_grade < 70:
#     print("C")
# if 50 <= number_grade < 60:
#     print("D")
# if number_grade < 50:
#     print("F")

# prints B (Works as intended)

# if number_grade >= 80:
#     print("A")
# elif number_grade >= 70:
#     print("B")
# elif number_grade >= 60:
#     print("C")
# elif number_grade >= 50:
#     print("D")
# elif number_grade < 50:
#     print("F")

# if number_grade >= 80:
#     print("A")
# elif number_grade >= 70:
#     print("B")
# elif number_grade >= 60:
#     print("C")
# elif number_grade >= 50:
#     print("D")
# else:
#     print("F")

def inspect_number(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else: 
        return "Zero"

print(inspect_number(0))

