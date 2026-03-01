class Person:
    def __init__(self , n ,o):
        print("Hey! you are the best Person")
        self.name=n
        self.occupation=o
        pass
    #name="Kreepa"
    #occupation="web Developer"


    def info(self):
         
        print(f"{self.name} is a {self.occupation}")

a= Person("Kreepa" , "Web Developer")
b= Person("Divya" , "Designer")
#a.name = "Divya"
#a.occupation = "Designer"
a.info()
b.info()


