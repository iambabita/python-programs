def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    

print(factorial(3))
print(factorial(2))
print(factorial(4))


# program to calculate fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))

print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i), end=" ")
