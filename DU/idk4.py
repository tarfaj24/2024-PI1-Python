a = int(input("zadaj číslo od: "))
b = int(input("zadaj číslo do: "))
print("     |", end = " ")
for i in range (a, b+1):
    print(f"{i:3}", end=" ")
print()
print("=====|"+("="*((b-a))*5))
for j in range(a, b+1):
    print(f"   {j:2}|", end= " ")
    for i in range(j*a, j*b+1, j):
        print(f"{i:3}",end =" ")
    print()

