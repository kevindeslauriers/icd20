# sum = 0
# for i in range(1,9,2):
#     sum += i
# print (sum)

# for i in range(10,0,-1):
#     print(i)


# for i in range(4,21,4):
#     print(i)

# for x in range(21):
#     if x % 4 == 0:
#         print(x)

# product = 1
# for i in range(1,6):
#     product *= i

# print(product)

# for i in range(3,13):
#     if i % 3 == 0:
#         print(i)

# for i in range(5,0,-1):
#     print(i)
# print("Blast Off!")

# import math

# for i in range(1,6):
#     print(math.pow(i,2))

# for i in range(1,6):
#     print(i*i)

# for i in range(1,6):
#     print(i**2)


# def factorial(n):
#     product = 1
#     for i in range (n,0,-1):
#         product *= i
#     return product

# for n in range(1,8):
#     print (factorial(n))

# str = "WONDERFUL"
# result = ""
# for i in range(1,len(str),2):
#     result += str[i]
# print(result)

# str = "COMPUTER".lower()

# count = 0
# for index in range(len(str)):
#     if str[index] in ('a', 'e', 'i', 'o', 'u'):
#         count += 1
# print(count)

backwards = ""
forwards = "RACECAR"

for index in range(len(forwards)-1, -1,-1):
    backwards += forwards[index]

if backwards == forwards:
    print("YES it is a Palindrome")
else:
    print("No it is not a Palindrome")

