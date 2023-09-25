age = 40
name = "Steve"

# print a line that says "I am Steve and I am 40 years old" using the variables age and name
print("I am " + name + " and I am " + str(age) + " years old.")
# I have to wrap non-string variables in str -> UGH! :(
# Alot of people / students have issues with all the opening and closing of "" and all the + variable + 
# It is MESSY!!!!!


print(f"I am {name} and I am {age} years old.")
# fstring are so much better (formatted strings)
# automatically changes variables to strings and no need to use + symbols



