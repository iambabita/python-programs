a=4
b="4"
print(a is b) #exact location of object in memory
print(a==b) #value

c=[1,2,3,4]
d=[1,2,3,4]
print(c is d)
print(c==d)

x = None
y="None"
if x is None:
    print(x is None)
    print(x==y)
