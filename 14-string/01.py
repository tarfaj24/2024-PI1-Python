# string je retazec znakou napr. "ahoj"
# retazec zaciname a koncime "" alebo ''
# \n - nový riadok. \t - tabulátor
# funkcia len() vráti dĺžku reťazca (dĺžku znakov)
# znaky v reťazci sú indexované prvý znak má index 0
#index piseme do hranatych zatvoriek alt f,g
retazec = "ahoj svet"
print(retazec)
print(len(retazec))
print(retazec[1])

# for i in range(len(retazec)):
#     print(retazec[i])

for znak in retazec: #postupne vybera znaky z retazca
    print(znak)