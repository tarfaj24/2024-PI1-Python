r = float(input("zadaj polomer: ")) #float je funkcia na prevod textu do desatinného čísla
# údajové typy: 
#    string - reťazec znakov (text)
#    int - celé čísla
#    float - celé čísla

O = 2 * 3.14 * r    # desatinné čísla uvádzame vždy s bodkou!!!
S = 3.14 * (r * r)
print ("Obvod kruhu je: ", round (O, 2)) #zaokrúhli číslo resp. premennú, O je premenná a 2 je počet desatinných miest
print ("Obsah kruhu je", round (S, 2)) 