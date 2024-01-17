#Q1 - Version
def count_vowels(str):
    num_vowels = 0
    vowels = "aeiou"
    for i in range(len(str)):   # using the index 0 .. len-1
        if str[i] in vowels:
            num_vowels += 1
    return num_vowels

#Q1 - Version 2
def count_vowels2(str):
    num_vowels = 0
    vowels = "aeiou"
    for i in str:       # if you iterate through a string it gets you each characters
        if i in vowels:
            num_vowels += 1
    return num_vowels

#Q2
def reverse_string(str):
    result = ''
    for i in range(len(str)-1,-1, -1):
        result += str[i]
    return result

#Q3
def remove_vowels(str):
    result = ''
    vowels = "aeiou"
    for i in str:       # if you iterate through a string it gets you each characters
        if i not in vowels:
            result += i
    return result



