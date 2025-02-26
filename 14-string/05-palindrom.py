#palindrom je retazec, ktorý je rovnaký pri čítaní od začiatku alebo od konca (abba)

ret = input("zadaj slovo: ")
obrateny = ret[::-1]
print(obrateny)

if ret == obrateny:
    print(f"Retazec {ret} je palindrom")
else:
    print(f"Retazec {ret} nie je palindrom")