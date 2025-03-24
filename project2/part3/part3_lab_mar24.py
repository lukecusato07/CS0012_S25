# Comments
'''
Please add comments to your code!

If there is a line or a section that is not clear, add a comments

Comments should write and read like quick bullet points

Format:
hashtag, space, capital letter
'''


# Dictionaries
my_list = [1, 2, 3, 4]

# Dictionaries have curly brackets

# Store key : value pairs
# Keys MUST BE unique, values do not have to be
my_dict = {}

# Key = first_name, Value = what you are bringing
picnic = {}

# Format to add:
# dict_name[key] = value
picnic["Scout"] = "Lofthouse cookies"
picnic["Julia"] = "Chips"

# This is okay --> their keys are unique
picnic["Kaitlyn"] = "Chips"

picnic["DeNardis"] = "Grapes"

print(picnic)
print("--"*25)

picnic["Julia"] = "Strawberries"

print(picnic)
print("--"*25)

# To delete from a dict:
# del dict_name[key]
del picnic["DeNardis"]

print(picnic)


# Iteration
# List example
nums = [1, 2, 3, 4]

for num in nums:
    print(num)
    
for p in picnic:
    print(p)
    
# To iterate over key : value pair --> .items()
print(list(picnic.items()))

# Format for iteration:
# for key, value in dict_name.items()
for person, snack in picnic.items():
    print(person, ":", snack) 


nums = [1, 2, 3, 4, 4, 2, 1, 1, 1, 3, 3, 2, 4]
freq = {}

for num in nums:
    if num not in freq:
        freq[num] = 1
    
    elif num in freq:
        freq[num] += 1
print(freq)
