from statistics import mode

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''

# How do we create a dictionary?
user_data = {"user_id":"400"}

print(type(user_data))
# Bracket notation


# Add new key value


# lets look at all the methods available to us


# lets try one


# Dict constructor


# Dictionary methods
# Lets use the keys methods to get the keys from this dictionary



# Lets use the values methods to get the values from this dictionary


# with an f string


# Lets use clear method to remove all elements


# Lets use get method to get a key value


# lets look at one of the parameters to show an error if the key doesnt exist


# Lets create a copy


# Lets remove a specified key with pop


# Lets remove a last inserted key-value pair with popitem


# Get a list with each key-value pair with items


# we can loop through


# Update dictionary


# Update can also update current key value pairs, as well as adding

# Dictionaries vs Lists
# list1 = ['a', 'b', 'c', 'd', 'e']
# dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}

# print(list1[3])  
# print(dict1[3])  

# list1[3] = 'z'
# dict1[3] = 'z'

# print(list1[3])  
# print(dict1[3])  

'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''

# Using zip and dict methods
# Zip creates a zip object


# Dict creates a dictionary

# my_keys = ['one', 'two', 'three']
# my_values = [4, 10, 30]


# Using dictionary comprehension

# my_keys = ['one', 'two', 'three']
# my_values = [1,2,3]



'''
Exercise

Write a dictionary that contains five words and their definitions. Then have your code print the word and their definition one at a time.
Hint: Use the items() method

'''


# As datasets, we can use bracket notation

# choices = {"flavors":['strawberry', 'vanilla', 'orange'],
#            "sizes":['large', 'medium', 'small']}


'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.

'''



'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''



'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''








 



