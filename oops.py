
class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Babita", 20)
student2 = Student("Ram", 22)

 
student1.display_info()
print(" ")
student2.display_info()