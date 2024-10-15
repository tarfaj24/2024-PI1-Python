n = int(input ("Zadaj N: "))
sucet = 0
for i in range(n):
    sucet = sucet + (i+1) # sucet + (i+1) je výraz, najskôr sa vypočíta výraz a výsledná hodnota sa priradí do premennej sucet
    # print(i, i+1, sucet)
print("Súčet prvých", n, "prirodzených čísel je,", sucet)