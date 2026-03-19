class employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance
        print(f"The dance is {self.dance}")


class Danceremployee(Dancer, employee):
    def __init__(self, dance, name):
        Dancer.__init__(self, dance)
        employee.__init__(self, name)

o = Danceremployee("Belly", "Swrikiti")

print(o)
print(o.name)
print(o.dance)

o.show()
print(Danceremployee.mro())



       
