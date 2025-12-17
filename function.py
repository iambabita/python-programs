def calculategmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

 
a=9
b=10
calculategmean(a,b)
if (a<b):
    print("first num is greater")
else:
    print("second num is greater")

gmean1=(a*b)/(a+b)
print(gmean1)
c=7
d=8
gmean2=(c*d)/(c+d)
print(gmean2)

#ADDITION OF TWO NUM:
def add(a, b):
    return a + b

 
def subtract(a, b):
    return a - b

 
def multiply(a, b):
    return a * b

 
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")
