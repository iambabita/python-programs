name = input("Enter your name: ")
marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\n----- Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 80:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")