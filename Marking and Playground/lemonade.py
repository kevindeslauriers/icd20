# get the weather function - the function will have a list and return a random choice (like hangman)

# get player input (how many cups of lemonade, adevertising signs, price per cup) 
# the first 2 we are spending $$, argument pass in the assetts (how much $$ you have)
# make sure they have the $$ to make the lemonade and  buy the signs
# update the assetts after you spend the $$

#counter for the day

# display the recap for the day
# how many you sold, how much you made (+ or -), current assests

import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



customers = random.randint(5,10)

print(customers)

weather = ["cold and sunny","hot and sunny","rainy"]
weather_multiplier = [2, 5, 0.2]

weather_type = random.randint(0,2)  # random number 0, 1 or 2

print(weather_type)     # print to see it
cls()
weath = weather[weather_type]
multiplier = weather_multiplier[weather_type]

print(weath)    # get the weather from the list with that index
print(multiplier) # get the weather from the list with that index

customers *= multiplier

print(customers)



# display instructions

#ask if they want to play again

#while(not gameover):
    # play 1 day of the game
    # ask if they want to play again
    # if no gameover = True
        








