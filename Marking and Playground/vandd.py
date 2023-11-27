import random # Imports random function so we can randomize health and damage
 
def create_character():
    char_health = random.randint(35, 70) # Randomizes health between a certain point
    char_name = input("Enter your character's name: ")
    print("Choose between these 3 classes (by their number 1-3)")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") # These 3 classes have special things to them that you will find out later
    class_choice = int(input("Enter your choice of class: "))
   
 
    if class_choice == 1:
        char_class = "Warrior"
        char_health = char_health + 20 # Adds a bonus to health based on class
        print("You have chosen the Warrior class! You get a +20 health bonus!")
   
    if class_choice == 2:
        char_class = "Mage"
        char_health = char_health + 10 # Adds a bonus to health based on class
        print("You have chosen the Mage class! You get a +10 health bonus!")
   
    if class_choice == 3:
        char_class = "Archer"
        char_health = char_health + 5 # Adds a bonus to health based on class
        print("You have chosen the Archer class! You get a +5 health bonus!")
 
    if class_choice not in [1, 2, 3]: # Shows the options that could have been
        char_class = "Warrior"
        print("Invalid class. You have been defaulted to warrior.") # If you did not choose a number to class, this defaults it to warrior
       
    return char_class, char_health, char_name
 
def game_intro(char_name, char_class):
    print(f"Hello {char_name}! You have woken up in a new, cyclops-filled world with the class of a {char_class}. Your health with your bonus is {char_health}!")
    print("Direction will be labelled by numbers.")
 
def end_game():
    print("Thank you for playing the Cyclops Adventure!")    
 
def encounter_scenario(char_class, current_health):
    received_totem = False
    print("You encounter a fork in the road. Which direction would you like to take?")
    print("1. Left")
    print("2. Right")
 
    direction = int(input("Please enter a number 1 or 2 based on the direction you would like to approach: "))
    if direction not in [1, 2]:
        print("You didn't go either direction. Are you scared? You are not allowed to go either direction now.")
        end_game()
 
    if direction == 1:
        print("You found a special totem! type the item's number when prompted to have the ability to use the item!")
        new_direction_after_1 = int(input("Where would you like to go now? (1 to return back and 2 to go right): "))
 
        if new_direction_after_1 not in [1,2]:
            print("Invalid entry. You decided to abandon your mission.")
            end_game()
           
 
        if new_direction_after_1 == 1:
            print("You decided to go home after retrieving the totem.")
            end_game()
            return
 
        if new_direction_after_1 == 2:
            direction = 2
            received_totem = True
 
    if direction == 2:
        print("You encountered a Cyclops? What would you like to do?")
        print("1. Fight")
        print("2. Use an item")
        print("3. Plead")
        fight_option = int(input("Please enter your choice: "))
 
 
 
        if fight_option == 1 and char_class == 'Warrior':
            print("You attacked the cyclops with your sword and attacked it! It is weakened but not out!")
            print("The cyclops attacked back!")
            cyclops_damage = random.randint(50, 100)
            manage_health(current_health, cyclops_damage)
           
            if current_health > 0:
 
                print("You are down but not out! What would you like to do now?")
                print("1. Fight")
                print("2. Use an item")
 
                fight_option_1a = int(input("Please enter your choice: "))
 
                if fight_option_1a == 1:
                    print("You attacked the cyclops with your sword and finished it off!")
                    end_game()
                    return
           
                if fight_option_1a == 2 and received_totem == True:
                    print("Which item would you like to use? You currently have 1 item.")
                    print("1. Totem")
                    item_use = input("Please enter the item of usage: ")
           
                    if item_use == 1:
                        print("You used your totem and vanquished the monster!")
                        end_game()
                        return
 
                    elif item_use not in [1]:
                        print("You got scared and didn't use an item and the cyclops killed you!")
                        end_game()
                        return
 
 
        if fight_option == 1 and char_class == 'Mage':
            print("You attacked the cyclops with your magic wand and attacked it! It is weakened but not out!")
            print("The cyclops attacked back!")
            cyclops_damage = random.randint(50, 100)
           
            manage_health(current_health, cyclops_damage)
           
            if current_health > 0:
 
                print("You are down but not out! What would you like to do now?")
                print("1. Fight")
                print("2. Use an item")
 
                fight_option_1a = int(input("Please enter your choice: "))
 
                if fight_option_1a == 1:
                    print("You attacked the cyclops with your staff and finished it off!")
                    end_game()
                    return
           
                if fight_option_1a == 2 and received_totem == True:
                    print("Which item would you like to use? You currently have 1 item.")
                    print("1. Totem")
                    item_use_1 = input("Please enter the item of usage: ")
           
                    if item_use_1 == 1:
                        print("You used your totem and vanquished the monster!")
                        end_game()
                        return
 
                    elif item_use_1 not in [1]:
                        print("You got scared and didn't use an item and the cyclops killed you!")
                        end_game()
                        return
           
 
        if fight_option == 1 and char_class == 'Archer':
            print("You shot the cyclops with your bow and arrow! You hit its eye and killed it!")
            end_game()
            return
 
 
         
        if fight_option == 2 and received_totem == True:
            print("Which item would you like to use? You currently have 1 item.")
            print("1. Totem")
            item_use = input("Please enter the item of usage: ")
           
            if item_use == 1:
                print("You used your totem and vanquished the monster!")
                end_game()
                return
 
            elif item_use not in [1]:
                print("You got scared and didn't use an item and the cyclops killed you!")
                end_game()
                return
 
        if fight_option == 2 and received_totem == False:
            print("You don't have any items to use! You wasted your time and the cyclops killed you.")
            end_game()
            return  
           
       
        if fight_option == 3:
            print("You tried to plead with the Cyclops and he didn't listen and used your head as a basketball! (he dunked that)")
            current_health = 0
            end_game()
            return
 
def manage_health(current_health, cyclops_damage):
    current_health = char_health - cyclops_damage
 
    print(f"Your damage taken during the encounter is {cyclops_damage}")
 
    print(f"Your current health after the fight is {current_health}")
   
    if current_health <= 0:
        print("You have died! Game Over! Your game has ended.")
        end_game()
        return
   
   
 
print("Welcome to my Game!")
char_class, char_health, char_name = create_character()
game_intro(char_name, char_class)  
encounter_scenario(char_class, char_health)
 
# direction, fight_option, fight_option_1a, item_use, class_choice, current_health =