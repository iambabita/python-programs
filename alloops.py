num = [20,30,40,60]

for i in range(len(num)//2):
    print(i)

    print("FOR LOOP: Print numbers 1 to 5")
for i in range(1, 6):
    print(i)

print("\nWHILE LOOP: Print numbers 6 to 10")
j = 6
while j <= 10:
    print(j)
    j += 1

print("\nDO-WHILE LOOP (Simulated): Print numbers 11 to 15")
k = 11
while True:
    print(k)
    k += 1
    if k > 15:
        break
