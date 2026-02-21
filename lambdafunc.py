def double(x):
    return x*2
#lambda x:x*2(same as above)
print(double(5))
cube=lambda x:x*x*x
print(cube(5))

avg= lambda x, y :(x+y/2)
print(avg(3,5))

def apple(fx , value):
    return 6+fx(value)
print(apple(cube , 2))
print(apple(lambda x:x*x*x , 2))


