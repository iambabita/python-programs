class Worker:
 def __init__(self):
        self.name = "They"
    
a=Worker()
a.workr1=10
print(a.name)

class Student:
    def __init__(self , age , name):
        self.age = age
        self.name = name
obj = Student(24 , "Sita")
print(obj.age)
print (obj.name)
        
class Student:
    def __init__(self, name, age, marks):
        self.name = name          # Public variable
        self._age = age           # Protected variable
        self.__marks = marks      # Private variable

    def display(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Marks:", self.__marks)


class Result(Student):
    def show_age(self):
        print("Accessing protected age:", self._age)


# Creating object
s1 = Result("Babita", 22, 85)

# Access through method
s1.display()

# Access protected variable in subclass
s1.show_age()

# Accessing protected variable outside class (possible but not recommended)
print("Protected Age:", s1._age)

# Accessing private variable (not directly allowed)
# print(s1.__marks)  # This will cause an error