numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))
print(result)
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
students = [("Ram", 22), ("Shyam", 18), ("Hari", 20)]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
add = lambda a, b: a + b
print(add(5, 3))
def multiply(x, y):
    return x * y
sum_three = lambda a, b, c: a + b + c
print(sum_three(2, 3, 4))