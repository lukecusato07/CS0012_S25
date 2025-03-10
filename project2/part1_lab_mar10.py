# Project 2 -- Part 1
'''
If you are having trouble dowloading the txt file
please download it in Chrome NOT Safari
'''


# Functions
# nytimes_news_articles_SMALL.txt

# Use def keyword
# Function name ~what the function does
def functionName(arg1, arg2, argN):
    # What the function does

def user_age():
    user_age = int(input("What is your age?: "))
    return user_age
    
    
def access(age):
    access = 0
    if age >= 21:
        access = 1
        print("You're in!")
    
    return access

def main():
    age = user_age()
    access(age)

# Must call main for our code to run!
main()


# Input()
# We allow the user to give the computer some info
    # This info helps us run our code
    
# Declare data type needed from user before declaring input()
user_input = int(input("What is your fav number?: "))

# Ex:
def myFunct():
    fav_number = int(input("Whjats your fav number"))
    
    return user_input

# For loops: count controlled
num = 1
# We tell python how many times to run the loop
for x in range(10):
    num += 1
    print(num)

print("---" * 50)
    

# This is how we will use for loops in project 2!
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)



# Files

# Let's open files as a variable name
open_file = open(file_name, "r", encoding = "utf-8")

# When opening a file, MUST close it when done
open_file.close()

for line in open_file:
    print(line)
    
    
# Slicing
f_name = "John"
l_name = "Smith"

# Format of a slice is: str_name[start:end+1]
if l_name[:] == "Smith":
    print("First name: ", f_name)
    
if f_name[0:2] == "Jo":
    print("First name is not Jack")

# Line 88 == line 92
if f_name[:2] == "Jo":
    print("First name is not Jack")





