import random # knižnica, ktorá slúži na generovanie náhodných hodnôt

nahodne_cislo = random.randint(1,10) # vygeneruje náhodné celé číslo v rozsahu 1 az 10
print(nahodne_cislo)

nahodna_farba = random.choice(["red", "green", "blue"]) # vygeneruje náhodnú hodnotu zo zoznamu hodnôt zoznam ohraničíme []
print(nahodna_farba)

nahodne_pismeno = random.choice("abcdefg") # vygeneruje náhodné písmeno
print(nahodne_pismeno)