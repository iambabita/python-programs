try:
    l=0,1,2,3,4,5,6,7
    i=int(input("enter the index:"))
    print(l[i])
except:
    print("Some error occured")
finally:
    print("I am already executed")
    