class Worker:
    def __init__(self , name , id):
        self.name =name
        self.id = id

    def showdetails(self):
     print(f"The name of the worker:{self.id} is {self.name}")

class Employee(Worker):
   def showlanguage(self):
      print("The default word is worker")


class Student(Employee):
   def showstudents(self):
      print("All the students are employeers")


      

w1 = Worker ("Her" , 230)
w1.showdetails()
w2 = Worker ("Him" , 231)
w2.showdetails()
e=Employee("Sita" , 110)
e.showlanguage()
s = Student("They" , 120)
s.showstudents()

        