with open ("file.txt",'r')as f:
    print(type(f))
    f.seek(20)
    print (f.tell())
    data=f.read(10)
    print(data)

with open ("file.txt",'w')as f:
    f.write("Hello World!!")
    f.truncate(3)

with open ("file.txt",'r')as f:
    print(f.read())