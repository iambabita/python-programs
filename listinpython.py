fruits=["Apple","Pineapple","Papaya","Guava","Lemon","Orange"]
print(fruits[0])
print(len(fruits[0]))
print(fruits[1])
print(len(fruits[1]))
fruits.insert(7,"orange")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.pop(2)
print(fruits)
if "Apple" in fruits:
    print("Apple is found")
else:
    print("Apple is not found")


if "Mango" in fruits:
        print("Mango is found")
else:
     print("Mango not found")
     