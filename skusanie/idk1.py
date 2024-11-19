cislo = int(input("zadaj cislo: "))
riadok = 1
sucet = 0
for i in str(cislo):
    cifra = int(i)
    print(f"{riadok}. cifra je: {i}")
    riadok = riadok + 1
    sucet = sucet + cifra
print("ciferny sucet je: ",sucet)