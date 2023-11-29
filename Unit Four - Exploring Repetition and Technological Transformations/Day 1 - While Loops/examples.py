import random

def print_1_to_n(n):
    count = 1

    while count <= n:
        print(count)
        count += 1


def get_user_info():
    user_input = ""

    while user_input.lower() not in ['yes', 'no']:
        user_input = input("Do you want to continue? (yes/no): ")
    
    return user_input

def guessing_game(lower, upper):
    target_number = random.randint(lower, upper)
    user_guess = 0

    while user_guess != target_number:
        user_guess = int(input(f"Guess the number ({lower}-{upper}): "))

    print("Congratulations! You guessed the correct number.")

def validate_password():
    correct_password = "secure123"
    entered_password = ""
    num_attempts = 0
    locked_out = False

    while num_attempts < 3 and entered_password != correct_password:
        num_attempts+=1
        entered_password = input("Enter the password: ")
        if num_attempts == 3 and entered_password != correct_password:
            print("Too many attempts. Login Failed.")
            locked_out = True

    return not locked_out
    
def select_option():
    valid_input = False
    while not valid_input:
        print("1. Print Hello")
        print("2. Print World")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Hello")
            valid_input = True
        elif choice == "2":
            print("World")
            valid_input = True

        elif choice == "3":
            print("Exiting the program.")
            valid_input = True
        else:
            print("Invalid choice. Please try again.")



# print_1_to_n(3)
# get_user_info()
# guessing_game(1,100)

# logged_in = validate_password()
# if logged_in:
#     print('Successful Login')
# else:
#     print('Unsuccessful Login')

select_option()






