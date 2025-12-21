def average(a,b):
    print ("The average is" (a+b)/2)
    average(3,6)
#Default value:dont take num is ok.
    def name(anyname,fname="Shyam", lname= "Hari"):
        print("Hello,",anyname,fname,lname)
        name("gita", "sweta","Jha")

        #KEYWORD ARGUMENT:
def average(a=9,b=1):
    print ("The average is" (a+b)/2)
    average(b=9)
    average(b=9,a=2)

    #FUNCTION ARGUMENT:
    #AT least one value should be taken.
def average(a,b,c=1):
    print("The average is :"(a+b+c)/2)
    average(5,6)


def average(*num):
    sum=0
    for i in num:
        sum=sum+i
        print("The average is:",sum/len(num))
        average(5,6,7,8,1)

def name(**name):
    print(type(name))
    print("Hello," ,name["fname"],name["mname"],name["lname"])
    name(fname="Krishna",mname="Kumar",lname="Karishma")

def average(*num):
    sum=0
    for i in num:
        sum=sum+i
        return(sum/len(num))
    d=average(4,5,6,7)
    print(d)









