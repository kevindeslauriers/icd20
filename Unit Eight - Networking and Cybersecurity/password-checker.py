def check_password_strength(password):
    # Define criteria for password strength
    length_requirement = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    common_passwords = ["password", "123456", "qwerty", "letmein", "abc123"]  # List of common passwords

    # Check length requirement
    if len(password) < length_requirement:
        return "Password is too short. It must contain at least {} characters.".format(length_requirement)

    # Check for uppercase, lowercase, digits, and special characters
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special_char = True

    # Check if password appears in list of common passwords
    if password.lower() in common_passwords:
        return "Password is too common. Please choose a different one."

    # Evaluate password strength based on criteria
    if has_uppercase and has_lowercase and has_digit and has_special_char:
        return "Password is strong."
    else:
        return "Password is weak. It must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."



# Prompt user to enter a password
password = input("Enter a password: ")

# Check password strength
strength_result = check_password_strength(password)
    
# Print the result
print(strength_result)



