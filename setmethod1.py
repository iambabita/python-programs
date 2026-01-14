
 
students = {"Ram", "Sita", "Gita", "Hari"}

print("Original set of students:")
print(students)

# Adding elements
students.add("Babita")
students.add("Anita")

print("\nAfter adding new students:")
print(students)

# Removing an element
students.remove("Hari")

print("\nAfter removing a student:")
print(students)

# Creating another set
new_students = {"Sita", "Anil", "Ramesh"}

print("\nNew students set:")
print(new_students)

# Using union method
all_students = students.union(new_students)
print("\nAll students after union:")
print(all_students)

# Using intersection method
common_students = students.intersection(new_students)
print("\nCommon students in both sets:")
print(common_students)

# Using difference method
different_students = students.difference(new_students)
print("\nStudents only in first set:")
print(different_students)
