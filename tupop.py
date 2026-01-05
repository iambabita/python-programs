countries=("Nepal", "China","Africa", "Canada")
temp= list(countries)
temp.append("Japan")
temp.pop(2)
temp[2]=("Australia")
countries=tuple(temp)
print(countries)


country1= ("Pakistan","Afganistan","Kazakhstan","Uzbekistan","Kyrgyzstan")
country2=("Nepal","Korea", "Bhutan")
Asia=country1+country2
print(Asia)


tuple1=(0,1,3,5,3,7,9)
res=tuple1.count(3)
print("count in tuple 3 is:", res)
res=tuple1.index(3)

res=tuple1.index(3,4,6)
res=len(tuple1)
