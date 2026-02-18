f=open('myfile.txt',"r")
i=0
while True:
 i=i+1
 line= f.readline()
 if not line:
  print(line , type(line))
 break
 

m1=line.split(",")[0]
m2=line.split(",")[1]
m3=line.split(",")[2]
print("marks of student (i) in maths is :{m1}")
print("marks of students ")
print(line)
if not line:
  print(line , type(line)) 

file=open('myfile.txt',"w")
lines=["line 1\n","line 2\n" ,"line 3\n"]
file.writelines(lines)
file.close()




 
 
 

