class employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

@classmethod
def fromstr(cls,string):
    return cls (string.split("-")[0] ,int( string.split[1]))

   
e= employee("Babita" , 1200)
print(e.name)
print(e.salary)

e1= employee("Babita" , 1200)
print(e1.name)
print(e1.salary)

string = "Babita - 1200"
e= employee(string.split ("-") , 1200)
print(e.name)
print (e.salary)

class person:
    def __init__(self , name , age):
        self.name= name
        self.age = age

    @classmethod
    def from_string(cls , string):
      name , age = string.split(",")
      return cls (name , int (age))
person = person.from_string("Shyam , 25")
print(person.name, person.age)

        

    

        