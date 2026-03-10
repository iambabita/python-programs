class employee:
    company = "Apple"
    def show (self):
        print(f"The name of the person is {self.name} and company is {self.company}")
        @classmethod
        def changecompany(cls , newcompany):
            cls.comapny = newcompany


e1=employee()
e1.name = "Babita"
e1.show()
e1.changecompany = ("BMW")
e1.show()
print(employee.company)
