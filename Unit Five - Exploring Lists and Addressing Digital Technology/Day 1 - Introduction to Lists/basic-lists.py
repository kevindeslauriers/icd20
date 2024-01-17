# Var = ["Geeks", "for", "Geeks"]
# print(Var)

# Python program to demonstrate
# Creation of List

# # Creating a List
# List = []
# print("Blank List: ")
# print(List)

# # Creating a List of numbers
# List = [10, 20, 14]
# print("\nList of numbers: ")
# print(List)

# # Creating a List of strings and accessing
# # using index
# List = ["Geeks", "For", "Geeks"]
# print("\nList Items: ")
# print(List[0])  # starts counting at 0 and this is the 1st element in the list
# print(List[2])  # prints the 3rd element in the list

# print(len(List))


list = []
list.append("hello")
list.append("Steve")
list.append("Abraham")
list.append("chicken")

print(list)
list.append(7)
print(list)

list.insert(2, "Dev")
print(list)
list.remove("chicken")
print(list)

who_left = list.pop(1)
print(list)
print(who_left)



