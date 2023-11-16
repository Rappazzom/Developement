# Do I need any modules? If so, as a best practice, import them at the top of the file
#  possibly use import re which imports regular expressions
'''
Project Description: Website Sign-Up
In this project, you will write a program that prompts a user to sign up for a website. The user must come up with a username and password, then log in using the username and password.
There are requirements for both the username and password. If either one doesn’t meet the requirements, print an appropriate error message and ask the username for a new username and password.
If they are both valid, store them as variables. Then ask the user to log in using the username and password they chose.
'''

# Problem: How should I start? 
# Solution: Your program should start with a print statement clearly explaining to the user both the username and password requirements. 
# Test, push code, test push code, test push code :)

# name = input(f"Hello user please tell me your name: ")

# print(f"Hello {name}, today we are going to help you set up a new username and password.\nLet me get started by stating the username requirements\nit must start with a lowercase letter\nonly contain letters, numbers, and underscores.\nWhile the password is at least 8 characters long\nContains at least one uppercase letter\nContains at least one lowercase\nletters Contains at least one digit\nContains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -\nDoesn’t contain any spaces ")
taken_names = 
error_1 = 'Your Username contains a capital letter, try again'
# Problem: The user must be continuously prompted for input.
# Solution(s): What tools do we have in place to facilitate this? If-then-else statements in conjunction with a while loop. 
# Test, push code, test push code, test push code :)
while True:
    user_name = input(f"Please enter your username here: ")
    has_uppercase = False
    for char in user_name:
        if char.isupper():
            has_uppercase = True
            break
    if has_uppercase:
        print(error_1)
    else:
        continue
    
    for char in user_name:
        if char.


# Problem: How are we managing error messages?
# Solution(s): We can serve error messages from strings in variables. We can serve error messages from a collection instrument such as a list or a tuple. Bad practice would be hardcoding error messages in our code. Though it works, it would be come difficult to handle and manage should a program be scaled up in the future or new error messages are added in the future with features. Handle this before you begin your while loop
# Test, push code, test push code, test push code :)



# Problem: How are we testing the username requirements?
# Solution(s): It must start with a lowercase letter and only contain letters, numbers, and underscores.
#   -String methods? Regular Expression? Both are acceptable solutions. Regex is more advanced and will save you a few lines of code
# Test, push code, test push code, test push code :)



# Problem: How are we testing password requirements?
# Solution(s): At least 8 characters long
#   Contains at least one uppercase letter
#   Contains at least one lowercase letter
#   Contains at least one digit
#   Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -
#   Doesn’t contain any spaces
#   -String methods? Regular Expression? Both are acceptable solutions. Regex is more advanced and will save you a few lines of code
# Test, push code, test push code, test push code :)


# Problem: How are we handling login process after successful sign up?
# Solution: With the assumption that after testing, the username and password fulfill requirements, we can reassign these values to more descriptive variables that are meant for the sign in and do a final test with a simple if else. Ternary operators are off the table as they cannot be used in a conditional expression.
# Test, push code, test push code, test push code :)


'''
These Git Commands are your best friends

git add . (what do I want to include in my next commit)
git commit -m"This is what I am doing" (captures your current changes before pushing)
git push (upload local repo to a remote repo)
git pull (fetches content from remote repo and updates your local repo to match)

'''







