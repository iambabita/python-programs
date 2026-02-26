class potato:
    employee="Surya"
    todo="Checking"
    price=250
    def info (self):
        print(f"{self.employee}'s work is to {self.todo}")

    

 
a=potato()
b=potato()
#TO CHANGE
#a.employee = "Bill"
#a.todo = "Packing"
b.employee = "peter"
b.todo = "cutting"

print(a.employee , a.todo , a.price)
a.info()
b.info()