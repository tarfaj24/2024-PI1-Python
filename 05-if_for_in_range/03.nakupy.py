pocet = 0
celkova_suma = 0
for suma in 1.5, 10.20, 25.30, 4, 5.50, 100:
     pocet = pocet + 1
     celkova_suma = celkova_suma + suma
     print(f"Suma {pocet}. nákupu: {suma}€")
print(f"Celkový počet nákupov: {pocet}")
print(f"Celková suma: {celkova_suma}")