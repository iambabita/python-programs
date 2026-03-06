 #PRIVATE VARIABLE:::
#Double underscore
class Program:
    def __init__(self):
        self._private_attribute = "I am a private attribute"
        self.__magnled_attribute = "I am a mangled attribute"

my_object = Program()
a=Program()
print(my_object._private_attribute)
print(my_object._Program__magnled_attribute)
print(a.__dir__())

class Student:
 def __init__(self , age , name):
    
  def __funName(self):  # An indication of private function
    self.y = 34
    print(self.y)

class Subject(Student):
    pass

obj = Student(21, "Harry")
obj1 = Subject

print(obj.__age)
print(obj.__funName())
 
print(obj1.__age)
print(obj1.__funName())

#PROTECTED:::
#Single underscore

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):   # protected method
        return "CodewithHarry"

class Subject(Student):  # inherited class
    pass

obj = Student()
obj1 = Subject()

print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())