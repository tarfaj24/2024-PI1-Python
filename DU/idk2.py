n = int(input("zadaj počet: "))
vysledok = 0
citatel = 4
for i in range(1, 2 * n, 2):
    vysledok = vysledok + citatel / i
    citatel = - citatel
print(vysledok)

