# Define a list
fruits = ['apple', 'banana', 'orange', 'kiwi']
numbers = [1,3,4,6,31,12,66]

# Check if 'banana' is in the list
if 'banana' in fruits:
    print('Yes, banana is in the list.')

# Check if 'grape' is in the list
if 'grape' not in fruits:
    print('No, grape is not in the list.')


is_in_numbers = 8 in numbers
print(is_in_numbers)



# Define a string
sentence = "Python programming is fun!"

# Check if 'programming' is a substring
if 'programming' in sentence:
    print('The word "programming" is present in the string.')

# Check if 'Java' is a substring
if 'Java' not in sentence:
    print('The word "Java" is not present in the string.')

# Define a string
sentence = "Python programming is fun!"

# Extract a substring from index 7 to 19
substring1 = sentence[7:20]
print(substring1)  # Output: "programming is"

# Extract the first 6 characters
substring2 = sentence[:6]
print(substring2)  # Output: "Python"

# Extract the last 4 characters
substring3 = sentence[-4:]
print(substring3)  # Output: "fun!"

print(sentence[2:]) #thon programming is fun! starts at index 2 and goes to the end
print(sentence[-2:]) #n! last 2 characters
print(sentence[:2]) #Py first 2 characters
print(sentence[:-2]) #Python programming is fu removes the last 2
print(sentence[2:-2])  #Starts at index 2 and removes the last 2


