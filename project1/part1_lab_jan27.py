from random import randint
# Comments
# Start a capital 

'''
Multi-Line 

comment
'''

"""
Multi-Line 

comment
"""

# Import
# ALWAYS go at the top
# from library import package

# Strings
"This is a string"

'This is also string'

'Stay consistent with choice of quotation marks!'

'Luke is 20'
'The first 3 digits of pi are 3.14'


# Print
print("Hello there!")


# Variables
# Anything that holds a value
# Assign with an = sign
age = 20         # Int
name = "Luke"    # Str

pi = 3.14       # Float

quote = "Try your best!"       # String
monday = True           # Boolean

# Underscore
cs_0012 = "Int computing ..."

# CamelCase
yourNameIs = "John Smith"

# Don't start name with uppercase
# No special chars

# Concatenation
# Combining of the strings
print(name)
# Comma reads like a sentence
print("My name is,", name, "and I am", age, "years old.") 

# Plus works like addition (adds it right on, no space)
print("My name is"+name)

# F string
print(f"My name is, {name} and I am {age} years old.")

# Input 
age = input("Enter your age: ")
print("The user is,", age, "years old.")
