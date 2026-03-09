class Math:
    def __init__(self, num):
        self.num = num

    def addinnum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b


#result = Math.add(1, 2)
#print(result)

a = Math(10)
print(a.num)

a.addinnum(6)
print(a.num)
print(Math.add(7,2))
 
