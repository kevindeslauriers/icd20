# #create a list
# list = [6,3,3,5,3,1,-9,-87,35,1,45,3]

# #iterate and print the list
# #print(list)
# # for element in list:    # element is the next element in the list (iterate every element in the list)
# #     print(element)      # works very similar to the range


# #get the sum of all of the numbers in the list (2 different ways)
# list = [1,2,3,4,5]
# total = 0
# for el in list:
#     total += el

# print(total)

# print("Another Way!")

# print(sum(list))    # sum() returns the sum of all the elements in the list

# #print only the positive even numbers in the list
# list = [6,3,3,5,3,1,-9,-87,35,1,45,3, -8, 10]
# print("Positive Even Numbers: ")
# for el in list:
#     if el % 2 == 0 and el > 0:
#         print(el)

# print("Get Smallest:")
# #get the largest and smallest number in the list
# smallest = list[0]  # assume the the first element is the smallest
# for el in list:     # go through the list
#     if el < smallest:   # check if this element is the new smallest
#         smallest = el   # if itis make it the smallest

# print(smallest)

# print("Get Biggest:")
# #get the largest and smallest number in the list
# biggest = list[0]  # assume the the first element is the biggest
# for el in list:     # go through the list
#     if el > biggest :   # check if this element is the new smallest
#         biggest = el   # if itis make it the smallest

# print(biggest)

# #another way
# print(min(list))
# print(max(list))



# #in a list of Strings, get the string that would be considered largest in terms of "alphabetical order"
# name_list = ["dev", "riya", "josh", "arees", "alexander", "abraham", "daniel", "zaafir", "ishaan"]
# # biggest_name = name_list[0]  
# # for el in name_list:     
# #     if el > biggest_name :   
# #         biggest_name = el

# # print(biggest_name) 

# print(max(name_list))   #zaafir
# print(min(name_list))   #abraham



# #work with min and max with strings upper and lower are different
# check = ["A","a"]
# print(max(check))



# #in a list of String, print the string with the longest length 2 ways
# longest = name_list[0]

# for el in name_list:
#     if len(longest) < len(el):
#         longest = el

# print(longest)

# print(max(name_list,key=len))   # using the key attribute we can change how to use max ()
# # print(max(name_list))


name_list = ["dev", "riya", "josh", "arees", "alexander", "abraham", "daniel", "zaafir", "ishaan", "123456789"]
longest = name_list[0]

for el in name_list:
    if len(longest) < len(el):
        longest = el

print(longest)  #length
print(max(name_list,key=len))   #length
print(max(name_list))   # alpha

print(ord("A")) # ord returns the ASCII value for the character



