# Coding:
# if the word contains atleast 3 characters, remove the first letter
# and append it at the end
# now append three random characters at the starting and the end
# else:
# simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last
# letter and append it to the beginning
# Your program should ask whether you want to code or decode
st=input("Enter a sentence:")
words=st.split(" ")
coding=True
if (coding):
    nwords=[]
    
    for word in words:

     if (len(word)>=3):
        p1="dfg"
        p2="lkfh"
        stnew=p1+ word[1:] +word[0]+p2
     else:
        nwords.append(stnew)
    print(" ". join(nwords)) 
    nwords=[]
    
    for word in words:

     if (len(word)>=3):
        p1="dfg"
        p2="lkfh"
        stnew=p1+ word[1:] +word[0]+p2
# Your program should ask whether you want to code or decode

st = input("Enter message")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False
print(coding)

if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)