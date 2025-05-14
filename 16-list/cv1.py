def postupnost(start,koniec,krok):
    zoznam = [start]
    postup = 0
    lastcislo = 1
    while True:
        if koniec > start:
            postup +=krok
            zoznam.append(start+postup)
            lastcislo = zoznam[len(zoznam)-1]
            if lastcislo >= koniec-krok:
                break
        if koniec < start:
            postup +=krok
            zoznam.append(start+postup)
            lastcislo = zoznam[len(zoznam)-1]
            print(lastcislo)
            if lastcislo <= koniec-krok:
                break
        
        
    return zoznam
print(postupnost(3, 100, 7))
print(postupnost(20, 0, -2))
print(postupnost(0, 3, 0.5))
