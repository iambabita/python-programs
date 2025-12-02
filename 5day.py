num1 = int(input("Enter any number: "))
num2 = int(input("Enter another number: "))
op = input("Enter yoour Opeator like + -, / X ")

if op == "+":
    result = num1+num2
elif op == "-":
    result =  num1-num2
elif op == "*":
    result = num1*num2
elif op == "/":
    result = num1/num2
else:
    result = "Invalid Opeator"

print(result)