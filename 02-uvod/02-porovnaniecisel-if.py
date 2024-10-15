a = int(input("zadaj číslo a: "))
b = int(input("zadaj číslo b: "))
if a > b:
    print("Väčšie je číslo", a)
else:
    print("Väčšie je číslo", b)
# if je podmienený príkaz
# najskôr zistí splnenie podmienky, ak platí tak sa vykonajú príkazy za dvojbodkou (odsadené od kraja)
# ak podmienka neplatí vykonajú sa príkazy za else: (odsadené od kraja)