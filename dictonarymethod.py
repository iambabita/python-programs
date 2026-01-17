ep1={122:45, 123:89, 222:33}
ep2={22:2 , 88:9 ,90:8}
ep1.update(ep2)
print(ep1)

st1={1:3,4:6,9:1}
st2={22:4,43:9,99:28}
st1.clear()
print(st1)

empty={}
print(empty)
ep1.pop(122)
print(ep1)
ep1.popitem()
print(ep1)

del ep1[222]
print(ep1)
