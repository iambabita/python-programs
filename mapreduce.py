#MAP
def cube (x):
    return x*x*x
print(cube (5))
l=[1,2,3,4,5,3,4]
newl=[]
for item in l:
    newl.append(cube(item))
    print(newl)

#SHORTCUT
newl=list(map(cube , l))
print(newl)

#FILTER
def filter_function(N):
 return N>4

newy=filter(filter_function , l)
print(newy)
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)


#REDUCE
from functools import reduce
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original List:", numbers)

 
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

 
squared_numbers = list(map(lambda x: x * x, even_numbers))
print("Squared Even Numbers:", squared_numbers)

 
sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)
print("Sum of Squared Even Numbers:", sum_of_squares)


