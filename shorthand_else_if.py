a=330
b=220

print("A") if a<b else print("=") if a==b else print("B")
c=9 if a>b else 0
print(c)

h=39803246
z=986713249095
print("This is great!") if h>z else print("This is okay!") if h==z else print("This is not success")

ram=("age :10" , "class=6" , "roll no.=2" , "Address=23RD")
shyam=("age :8" , "class=5" , "roll no.=19" , "Address=23RP")
print("Ram is not found") if ram>shyam else print("Ram is there") if ram==shyam else print("Ram is found")

o=("Sita" , 20 , "Nepali")
p=("sam" , 16 , "Indian")
print("Yes! she is eligible") if p<o else ("No! she is not eligible") if o==p else print("She is eligible")