
#Q1 - While Loops
n = int(input('Please enter a positive'))
while n <= 0: # while n is not positive
    n = int(input('Please enter a positive'))

#Q2 - While Loops
import random
n = random.randInt(1,10)

guess = 0
while guess != n:
    guess = int(input('Enter your guess: '))
    if guess < n:
        print('Too Low')
    elif guess > n:
        print('Too High')
    else:
        print('Correct')


#Q3 - While Loops
n = 2
sum = 0

while n <= 10:
    sum += n
    n += 2

print(sum)
