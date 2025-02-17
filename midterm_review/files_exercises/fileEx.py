# File example
# To open a file:
    # format: varName = open("fileName.txt", method)

# Mode "w"
writeFile = open("write.txt", "w")

# Format to write: varName.write("Mesage")
writeFile.write("This is CS0012 Lab")

# Must always close a file
writeFile.close()

# Mode "r"
readFile = open("read.txt", "r")

print(readFile.read())  # Prints file contents
readFile.close()

# Mode "a"
appendFile = open("append.txt", "a")
appendFile.write("\n\t- Example: Adding to my notes about mode 'a'")
appendFile.close()

# Readline
writeFile = open("write.txt", "r")

print(writeFile.readline())
writeFile.close()


# Another method to read each line in the file
writeFile = open("write.txt", "r")

for line in writeFile:
    print(line)

writeFile = open("write.txt", "r")



# Format: fileName.close()
writeFile.close()
