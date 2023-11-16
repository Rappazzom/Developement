# Define the requirements for username and password
username_requirements = "Username must start with a lowercase letter and only contain letters, numbers, and underscores."
password_requirements = "Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one of these characters: !, ?, @, #, $, ^, &, *, _, -."

# Function to check if a username is valid
def is_valid_username(username):
    return username[0].islower() and username.isalnum() and '_' in username

# Function to check if a password is valid
def is_valid_password(password):
    return len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in "!?@#$^&*_- " for char in password)

# Prompt user for username
while True:
    user_name = input("Please enter your username: ")
    if is_valid_username(user_name):
        break
    else:
        print("Invalid username. " + username_requirements)

# Prompt user for password
while True:
    user_password = input("Please enter your password: ")
    if is_valid_password(user_password):
        break
    else:
        print("Invalid password. " + password_requirements)

# Store username and password as variables
stored_username = user_name
stored_password = user_password

# Ask user to log in
while True:
    login_username = input("Please enter your username to log in: ")
    login_password = input("Please enter your password to log in: ")
    
    # Check if the entered username and password match the stored values
    if login_username == stored_username and login_password == stored_password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Please try again.")
