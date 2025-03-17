# How comments should not look:
nums = [1,2,3,4,5,6,7]  # This is a list. Lists are made with hard brackets and contain things seperated by commas


for num in nums:        # The first thing that I am going to do is write a for loop
    while num < 5:      # I also need to write another loop here

        operation = num**3  # This is what I am doing to the number
        print(operation)


        break   # The last thing that I am doing in the code is stop the loop

# How comments should look:
nums = [1,2,3,4,5,6,7]

for num in nums:        # Looping over each number in the list
    while num < 5:      # Isolating all numbers less than 5

        operation = num**3  # Cubing the number
        print(operation)


        break   # Stopping the loop so it doesn't run infinitely

# Lines that don't need comments:
print("Hello, world!")
name = "John, Smith"
age = 21
pi = 3.141592653589
