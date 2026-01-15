set1={1,2,3,4,5,6,7,8,9}
set2={10,11,12,13,14,15,16,17,18,19}
print(set1.union (set2))
set1.update(set2)
print(set1,set2)

cities={"Tokyo","Kathmandu","Barcelona"}
cities2={"Tokyo", "Kabul","Barcelona"}
cities3= cities.union(cities2)
print(cities3)
cities4=cities.intersection(cities2)
print(cities4)
cities.intersection_update(cities2)
print(cities)
cities.symmetric_difference(cities2)
print(cities)
fruits={"Pineapple","papaya", "apple"}
fruits2={"Banana","Mango","apple"}
print(fruits.isdisjoint(fruits2))
print(fruits.issuperset(fruits2))
print(fruits.issubset(fruits2))
fruits.add("Melon")
print(fruits)
fruits.remove("papaya")
print(fruits)
fruits.discard("Melon2")
print(fruits)
healthy=fruits.pop()
print(fruits)
print(healthy)


info={"Carla",19,False,19.5}
if "Carla" in info:
    print("Carla is present")
else:
    print("Carla is absent")
    

