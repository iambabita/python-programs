x=[1,2,3,4,5]
print(dir(x))
print(x.__add__)
class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        self.version = 3 
p= person("Babita ", 19)
print(p.__dict__)
print(help(person))

#Parent class
class parent:
    def parent_method(self):
        print("This is the parent method")

class childclass(parent):
    def parent_method(self):
        print("Babita")
        super().parent_method()

    def child_method(self):
        print("This is a child method")
        super().parent_method()   # correct spelling

child_object = childclass()
child_object.child_method()
child_object.parent_method()


class employee:
    def __init__(self, name , id):
        self.name = name
        self.id = id

class programmer(employee):
    def __init__(self , name , id , language):
        self.name = name
        super().__init__(name , id)
        self.language = language
         


Nisha = employee("Nisha" , 30)
Babita = programmer("Babita" , 20 , "Python")
print(Babita.name)
print(Babita.id)
print(Babita.language)

        
