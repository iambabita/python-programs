dict = {
    "Python" : "the best programming language",
    "spoon":"Object"
}
print(dict["Python"])

id={
    123:"Sweta",
    234:"Manoj",
    901:"Zalkir",
    224:"Zack"
    
}
print(id[123])

info={'name':"Karan", "roll":34,  "eligible":"Yes"}
print(info)
print(info["name"])
print(info.get("eligible"))
print(info.values)


for key in info.keys():
    print(info[key])
    print(f"The value corresponding to key{key}is{info[key]}")
print(info.items())
for key, value in info.items():
    print(f"The value corresponding to key{key}is{value}")




    