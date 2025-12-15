# Program to find sum and average of numbers
 

print("Sum and Average Program")

n = int(input("How many numbers do you want to enter? "))

total = 0

 
for i in range(1, n + 1):
    num = int(input(f"Enter number {i}: "))
    total = total + num

# calculate average
average = total / n

print("Total sum is:", total)
print("Average is:", average)

 
if total % 2 == 0:
    print("The sum is even")
else:
    print("The sum is odd")

print("Program finished")
