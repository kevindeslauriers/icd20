#Q1 - For Loops
sum = 0
for i in range(1,21):   # start at 1, stops at 20 and counts by 1
    if i % 2 == 0:
        sum += i

print(sum)

#Q1 - For Loops - Version 2
sum = 0
for i in range(2,21,2):   # start at 2, stops at 20 and counts by 2
        sum += i

print(sum)

#Q2 - For Loops
letter = input("Please enter a letter: ")
n = int(input("Enter a number: "))
result = ''
#for i in range(0, n):
#for i in range(n):  # by default it starts at 0 (0, 1, 2, 3, n-2, n-1)
for i in range(1, n+1): #also works 
     result += letter
     #result = result + letter

print(result)

#Q3 - For Loops
for i in range(8,0,-1):     #range(start, end, increment) -> don't include end
     print(i)

