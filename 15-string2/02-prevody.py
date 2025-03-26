# print(bin(255)) # vypíše číslo v binárnej podobe
# print(hex(255)) # vypíše číslo v binárnej podobe
# print(0b11111111)#vypíše binárne číslo v desiatkovej hodnote
# print(0b11111111)#vypíše hexadecimálne ČÍSLO v desiatkovej podobe

cislo = int(input("zadaj cislo: "))

def dec_bin(cislo):
    bincislo = ""
    while cislo > 0:
        zvysok = cislo % 2
        bincislo = str(zvysok) + bincislo
        cislo = cislo // 2
    return bincislo



def dec_hex(cislo):
    hexcislo = ""
    while cislo > 0:
        zvysok = cislo % 16
        if zvysok < 10:
            hexcislo = str(zvysok) + hexcislo
            # if zvysok == 15:
            #     zvysok = "F"
            # elif zvysok == 14:
            #     zvysok = "E"
            # elif zvysok == 13:
            #     zvysok = "D"
            # elif zvysok == 12:
            #     zvysok = "C"
            # elif zvysok == 11:
            #     zvysok = "B"
            # elif zvysok == 10:
            #     zvysok = "A"
        else:
            hexcislo = chr(55+zvysok) + hexcislo
        cislo = cislo // 16
    return hexcislo

def dec_oct(cislo):
     octcislo = ""
     while cislo > 0:
         zvysok = cislo % 8
         octcislo = str(zvysok) + octcislo
         cislo = cislo // 8
     return octcislo


print(dec_bin(cislo))
print(dec_hex(cislo))
print(dec_oct(cislo))



