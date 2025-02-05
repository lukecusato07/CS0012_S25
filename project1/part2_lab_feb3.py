# Project 1 Part 2 introduces if statements

'''
- If statements are a set of decision statements for the
computer to evaluate and execute if true

- There are the following if statements:
    if, elif (else-if), and else

- Formatting:

if statement(s)_to_be_evaulated:
    do this
    
- Must have if, then statement, then colon, 
then indent on next line

- If statements can evaluate multiple statements using and/or
    - *when writing and/or we do not put them in quotation marks*
    
- and: both statements must be true to trigger
- or: either or both statements can be true to trigger
'''

# Let's run a mock program to get into a bar
age = 21

# First statement is always if
if age < 21:
    print('You are too young. Access denied!')

# Every next statement except for the last is always elif
elif age > 21:
    print('You are old enough. Access granted!')

# Last statement is always else
else:
    print('You are 21. Access granted!')
    
# Which one of these statements do you think will trigger?


# We can also simplify and write it like this
age = int(input('Please enter your age for access to the club: '))

# We use or because either statement grants access
if age == 21 or age > 21:
    print('You are old enough. Access granted!')

else:
    print('You are too young. Access denied!')
    
# Can you think of some real life scenarios where you can use if statements?


# Here's how we can use and
name = 'Luke'
taken_class_before = True

if name == 'Luke' and taken_class_before:
    role = 'Teaching assistant'
    
else:
    role = 'Student'
  
print('The user is a', role, '.')
