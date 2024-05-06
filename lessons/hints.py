# Importing Keywords
import keyword
# print(keyword.kwlist) - List of Python keywords

# Naming Conventions
# snake case - ex. hello_world
# screaming snake case - HELLO_WORLD

# Basic Data Types
# none - Represents null
# boolen_type - Boolean variable
# int - Integer
# float - Floating point number
# list - List
# tuple - Tuple
# range - Range
# str - String
# set - Set
# frozen - Immutable set
# dict - Dictionary

# Data Type Categories
# mutable - list, dict, set
# immutable - int, float, str, bytes, etc.

# Examples of Using Data Types
# Dictionary example
my_dict = {1: "my_string"}
# Changing value in dictionary
my_dict[1] = 1.1

# List example
my_list = ['abc', 1]
# Changing an element in a list
my_list[1] = "dodo"

# Tuple example
my_tuple = (1, 2, 3)

# Range example
# range(1, 10) - From 1 to 9

# String examples
string = 'hell'  # Single quotes are generally a good practice
# Dictionary usage in a string with f-string
my_dict = {'key': "my_string"}
string = f"demonstration{my_dict['key']}"

# Set examples
my_set = {"demonstration", 10, "string"}  # Unordered, duplicates not saved

# Simple arithmetic operations
my_value = 10
my_value += 5
if my_value is True:
    print("my_value is True")

# Type casting and type checking
my_int = 10
my_float = 10.1
summary = my_int + my_float
print(type(summary))  # Will only return the most complex type.

# Converting int to string
print(type(str(my_int)))

# Converting list to set and printing set
my_list = [10, 11, 25, 13]
my_set = set(my_list)
print(my_set)

# Simple arithmetic on a variable
my_list = 10
my_list += 11
print(my_list)  # Simple way to use arithmetic operators

# If-else structure
my_list = 11
if my_list == 10:
    print("Hello")
else:
    print("Hello1")

# If-elif-else structure
my_list = 21
if my_list == 10:
    print("Hello")
elif my_list == 20:
    print("Hello1")
else:
    print("Hello2")

# Boolean expression example
value = 0
print(value <= 10)  # true/false

# While loop example
value = 0
while value <= 3:
    print(value)
    value += 1

# For loop over a list
my_list = [1, 2, 3]
for list_values in my_list:
    print(list_values)

# Simple for loop with a range
sum_n = 0
for value in range(0, 3):
    sum_n += value
    print(value)
