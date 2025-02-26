#string v pythone je immutable,tzv. nemeniteľný
ret = "Ahoj svet"
# ret[0] = "a" #toto nie je v Pythone možné lebo je to immutable
ret = "a" + ret[1:] #ak chceme zmenit nejaký retazec musíme to urobit takto
print(ret)

#retazce vieme porovnávať

print("wadsada" == "wads")
print("wadsada" > "wads")
print("a" > "A")

print(ord("A")) #ord() je funkcia, ktorá vráti ordinálnu (číselnú) hodnotu

print(chr(65)) #chr() je funkcia, ktorá na základe ordinálnej hodnoty vráti znak