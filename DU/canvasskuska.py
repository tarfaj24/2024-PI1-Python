cislo = int(input('Zadaj číslo: '))
pocet = 0
print('delitele:', end=' ')
for delitel in range(1, cislo + 1):
    if cislo % delitel == 0:        # mohli by sme zapísať aj  if not cislo % delitel:
        pocet += 1
        print(delitel, end=' ')
print()
print('počet deliteľov:', pocet)