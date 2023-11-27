import random

def create_character():
    print("Welcome to the Simple Python Adventure Game!")
    character_name = input("Enter your character's name: ")

    # Choose a character class
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    class_choice = input("Enter the number of your choice (1-3): ")

    # Validate class choice
    while class_choice not in ['1', '2', '3']:
        print("Invalid choice.")
        print("Choose your character class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        class_choice = input("Enter the number of your choice (1-3): ")
  
    if class_choice == '1':
        character_class = 'Warrior'
    elif class_choice == '2':
        character_class = 'Mage'
    else:
        character_class = 'Archer'

    # Set initial health between 50 and 100
    initial_health = random.randint(50, 100)

    return character_name, character_class, initial_health

def game_intro(character_name, character_class):
    print(f"Welcome, {character_name} the {character_class}!")
    print("You find yourself in a mysterious world. Prepare for an adventure!")

def make_decision():
    print("You reach a crossroads. What do you want to do?")
    print("1. Go left")
    print("2. Go right")
    decision = input("Enter the number of your choice (1 or 2): ")

    return decision

def encounter_scenario(direction):
    if direction == '1':
        print("You encounter a friendly creature. It gives you a gift!")
        return 10  # Bonus points for a friendly encounter
    elif direction == '2':
        print("You face a challenging enemy. Prepare for a battle!")
        return -20  # Penalty for facing an enemy
    else:
        print("Invalid choice. No bonus or penalty.")
        return 0

def manage_health(current_health, damage_taken):
    new_health = current_health + damage_taken
    if new_health <= 0:
        print("Game over! Your health is too low.")
    else:
        print(f"Remaining health: {new_health}")

def game_completion():
    print("Thanks for playing the Simple Python Adventure Game!")

def main():
    # Task 1: Character Creation
    name, char_class, health = create_character()

    # Task 2: Game Introduction
    game_intro(name, char_class)

    # Task 3: Decision Making
    decision = make_decision()

    # Task 4: Encounter
    damage = encounter_scenario(decision)

    # Task 5: Health Management
    manage_health(health, damage)

    # Task 6: Bonus Points (Optional)
    # Task 7: Game Completion
    game_completion()

# Run the game
main()
