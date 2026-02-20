 
file = open("example.txt", "w")

file.write("Hello Babita!\n")
file.write("Welcome to Python file handling.\n")
file.write("You are learning readlines and write methods.\n")

file.close()

# Reading data from the file using readlines()
file = open("example.txt", "r")

lines = file.readlines()

print("Reading file using readlines():\n")

for line in lines:
    print(line.strip())

file.close()
