# How To: Midterm Coding Section
'''
- I need to get the user's age
    - To get user input --> input()
    - I need age --> int(input())

- Check the user's age against the drinking age (21)
    - Comparisions --> >=, <=, or ==
- Then grant/deny access
    - Comparision + action --> if/elif

- After the first user, generate a random num to see how many people are left
    - Generate random num --> randint()
    - Import this library on line 1

- Run the simulation for remaining people unless there are none
    - While there are people left:
        - Run simulation
    --> while loop to do this
'''

from random import randint

def getAge():
    userAge = int(input("How old are you?: "))
    
    return userAge
    
    
def grantAccess(userAge):
    # 0 --> denied
    access = 0
    
    if userAge >= 21:
        # 1 --> granted
        access = 1
        print(access, ": You are old enough!")
    
    else:
        access = 0
        print(access, ": You are not old enough!")
        
    return access
    
    
def numInLine():
    lineLength = randint(0,10)
    
    return lineLength
    
    
def main():
    # Step 1: Get first user's age
    ageInput = getAge()
    
    # Step 2: Grant/deny access
    userAccess = grantAccess(ageInput)
    
    # Step 3: Generate random num
    lineLen = numInLine()
    
    # Step 4: While there are people left, run simulation
    while lineLen > 0:
        print("There are", lineLen, "people still in line.")
        # Step 1: Get first user's age
        ageInput = getAge()
        
        # Step 2: Grant/deny access
        userAccess = grantAccess(ageInput)
        
        lineLen -= 1

main()
