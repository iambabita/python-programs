# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original list:", fruits)

# 1. append() – add item at the end
fruits.append("Grapes")
print("After append:", fruits)

# 2. insert() – add item at a specific position
fruits.insert(1, "Papaya")
print("After insert:", fruits)

# 3. remove() – remove specific item
fruits.remove("Mango")
print("After remove:", fruits)

# 4. pop() – remove item by index
fruits.pop(2)
print("After pop:", fruits)

# 5. index() – find index of an item
print("Index of Apple:", fruits.index("Apple"))

# 6. count() – count how many times item appears
fruits.append("Apple")
print("Count of Apple:", fruits.count("Apple"))

# 7. sort() – sort the list
fruits.sort()
print("After sort:", fruits)

# 8. reverse() – reverse the list
fruits.reverse()
print("After reverse:", fruits)

# 9. len() – length of list
print("Total items:", len(fruits))

# 10. clear() – remove all items
fruits.clear()
print("After clear:", fruits)
