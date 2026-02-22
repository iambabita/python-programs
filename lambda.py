numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))
print(result)
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
students = [("Ram", 22), ("Shyam", 18), ("Hari", 20)]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)