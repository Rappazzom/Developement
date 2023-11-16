'''
Fun Facts about Sets

-unordered, unchangeable*, and unindexed.
* The items are unchangeable, but you can add and remove items.
Sets do not allow duplicates, so they are used to store a set of unique values. You use curly brackets for sets: { }
Because sets are unordered, you can't index them like a list. They don't have indexes at all. You can still loop through a set with a for loop.

'''

# Create a set
# i_am_empty = set()
# print(i_am_empty)

# What am I?
# check_my_type = {}
# print(type(check_my_type))

# Pass in a list
# my_fav_colors_list = ['green', 'blue', 'red']
# my_fav_colors_set = set(my_fav_colors_list)
# print(my_fav_colors_set)

# Unordered
# my_unordered_set = {'blue', 'green', 'red', 'orange'}
# print(my_unordered_set)

# Unchangeable
# my_unchangeable_set = {'hello', 'welcome', 'to', 'newyork'}
# my_unchangeable_set[3] = 'newjersey' # Doesn't work in a set only a list

# Unindexed
# my_unindexable_set = {'I', 'cant', 'be', 'indexed'}
# print(my_unindexable_set[2]) # you can't index a set
# Break up a string
# first_name = set('Mike')
# print(first_name)
# first_name = {'Mike'}
# print(first_name)


# No duplicates allowed
# my_cars = ['chevy', 'toyota', 'ford', 'ford', 'honda', 'honda']
# my_unique_cars = list(set(my_cars))
# print(my_unique_cars)

# No duplicates - How did we solve this problem before?
# no_dupes = []

# for i in my_cars:
#     if i not in no_dupes:
#         no_dupes.append(i)
# print(no_dupes)

'''
8. Exercise: Removing All Duplicates
You have a list storing important data for your company, but it contains some duplicate entries. 
Go through your list and remove all the duplicates. When you're done, each item should appear in 
the list exactly once.
'''
''' With a for loop and appending'''

#original list
# states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']
# my_states = set(states)
# print(my_states)
# # # this will capture our unique states
# states_no_duplicates = []
# for i in states:
#     if i not in states_no_duplicates:
#         states_no_duplicates.append(i)
# print(states_no_duplicates)
'''we will loop through states, and append only the first occurence of each state into our empty list'''

# for s in states:
#     if s not in states_no_duplicates:
#         states_no_duplicates.append(s)
# print(states_no_duplicates)

''' With sets and returning a list '''

# states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']
# my_states = list(set(states))
# print(my_states)

# We can loop through sets
# top_ten_movies = {'shawshank redemption', 'avatar', 'avengers', 'its a wonderful life'}
# for t in top_ten_movies:
#     print(t)
# Lets look at some methods

# Let's add silver .add()
# colors = {'blue', 'green', 'red'}
# colors.add('silver')
# print(colors)

# Lets clear all our items .clear()
# transportation = {'cars', 'bikes', 'plane'}
# transportation.clear()
# print(transportation)


# Lets create a copy into a set called comedy .copy()
# sitcoms = {'friends', 'seinfeld', 'honeymooners'}
# comedy = sitcoms.copy()
# print(comedy)
# print(sitcoms)

# # Remove vermont from our set # lets user know its in there. if its not there it flags an error
# states = {'california', 'new york', 'vermont', 'connecticut'}
# states.remove('vermont')
# print(states)

# Remove vermont from our .discard # discards string regardless if its there or not

# states = {'california', 'new york', 'vermont', 'connecticut'}
# states.discard('vermont')
# print(states)

# Difference - What's different?       -   -   -   the minus sign is how you find difference

# student_set = {'judith', 'majestic', 'samuel'}
# student_set_2 = {'judith', 'majestic', 'mike'}
# result = student_set_2 - student_set # Operator 
# result2 = student_set.difference(student_set_2)
# print(result)

# Intersect - What do we have in common? &

# my_schedule = {'mon', 'wed', 'thurs'}
# majestik_schedule = {'wed', 'fri', 'sat'}
# meet = my_schedule & majestik_schedule
# print(meet)

# meet2 = my_schedule.intersection(majestik_schedule)
# print(meet2)

# Union - All pets that appear in any set  |

# reynelles_pets = {'dog', 'cat', 'bird'}
# julie_samuels_pets = {'chickens', 'dog', 'fish'}
# kat_pollans_pets = {'bird', 'dog', 'fish'}
# majestic_pets = {'turtle'}
# pets = reynelles_pets | julie_samuels_pets | kat_pollans_pets | majestic_pets
# print(pets)

# pets2 = reynelles_pets.union(julie_samuels_pets, kat_pollans_pets, majestic_pets)
# print(pets2)

# Symmetric difference - Items outside of matching items ^

# robins_books = {'catcher in the rye', 'richest man in babylon'}
# anthonys_books = {'catcher in the rye', 'richest man in babylon', 'sounder'}

# books = robins_books ^ anthonys_books
# print(books)

# books2 = robins_books.symmetric_difference(anthonys_books)
# print(books2)
'''
Exercise - Sets
You work for a sales company and must generate a set of all customers who get a certain discount. The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
You have a set of customers over 60, and a set of customers who have made at least 5 purchases. Use a set operation to output a set of customers that fit both criteria for the discount. You can do this in one line of code.
Example:
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}
Output: {'Dominic', 'Simone'}
'''

# Solve with 1 or 2 lines of code

# over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
# over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}
# discount = over_60_years & over_5_purchases
# print(discount)

'''
Exercise - Sets
You work at a company where some people know Python, some people know JavaScript, and some people know both.
In a loop, prompt the user to input an employee name, whether they know Python, and whether they know JavaScript. Use this to build two sets: a set of employees that know Python, and a set of employees that know JavaScript.
Use set operators to compute the following sets:
The set of employees that know both Python and JavaScript
The set of employees that know JavaScript, but not Python
The set of employees that know Python or JavaScript, but not both
'''

# Framework for my comments

# My set variables

knows_java = set()
knows_python = set()
knows_java_and_python = set(knows_java) & set(knows_python)
# User input variables
# python = input(f"Enter emplyees name that know python: ")
# java = input(f"Enter employee name that know Java: ")
# Error messages
stop_reminder = print(f"Please enter 1 employee name at a time")
intructions = print(f'Type stop once you have finished')
while True:
    python = input(f"Enter emplyees name that knows python: ")
    if python.lower() == 'stop':
        break
    knows_python.add(python)
while True:
    java = input(f"Enter employee name that know Java: ")
    if java.lower() == 'stop':
        break
    knows_java.add(java)

knows_java_and_python = set(knows_java) & set(knows_python)



knows_java_and_python = knows_java.intersection(knows_python)
knows_java_not_python = knows_java.difference(knows_python)
knows_either_java_or_python = knows_java.symmetric_difference(knows_python)

print("Employees who know both Java and Python:", knows_java_and_python)
print("Employees who know Java but not Python:", knows_java_not_python)
print("Employees who know either Java or Python, but not both:", knows_either_java_or_python)

# #My data collection
# python_devs, js_devs, = set(), set()

# #user input
# dev_type_input, dev_name_input = '' , ''

# error_msgs = ('Invalid input, please try again.','Thank you, Have a nice day.')

# while True:
#     dev_type_input == 'p' or dev_type_input == 'j'



