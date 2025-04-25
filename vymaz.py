import random

moznosti = {
    "párne": None,
    "nepárne": None,
    "vyber": None,
    "vyhra": None,
    "prehra": None,
}

def betting_system():
    global amount
    global bet
    starting_amount = 1000
    amount = starting_amount
    print(f"Tvoj stav je: {amount}")

def hrac():
    global amount
    global bet
    moznosti["párne"] = 2
    moznosti["nepárne"] = 1

    while amount > 0:  
        while True:
            try:
                bet = int(input("Zadaj koľko chceš staviť: "))
                if bet > amount:
                    print("Nedostatok na účte.")
                elif bet <= 0:
                    print("Stávka musí byť kladné číslo.")
                else:
                    print(f"Stavil si {bet}.")
                    break
            except ValueError:
                print("Zadaj platné číslo.")

        odpoved = random.choice([moznosti["párne"], moznosti["nepárne"]])
        print("Stlač [1] pre párne")
        print("Stlač [2] pre nepárne")
        print("Stlač [3] pre stop")

        while True:
            try:
                vyber = int(input("Vyber si jednu z možností: "))
                if vyber == 1:
                    moznosti["vyber"] = moznosti["párne"]
                    break
                elif vyber == 2:
                    moznosti["vyber"] = moznosti["nepárne"]
                    break
                elif vyber == 3:
                    print("Hra bola ukončená.")
                    return
                else:
                    print("Iba [1], [2] alebo [3].")
            except ValueError:
                print("Zadaj platné číslo [1], [2] alebo [3].")

        print(f"Padlo číslo: {odpoved}")

        if moznosti["vyber"] == odpoved:
            moznosti["vyhra"] = moznosti["vyber"]
            print("Vyhral si!")
            amount += bet
        else:
            moznosti["prehra"] = moznosti["vyber"]
            print("Prehral si.")
            amount -= bet

        print(f"Tvoj nový zostatok je: {amount}")

        if amount <= 0:
            print("Nemáš dostatok peňazí na pokračovanie. Hra končí.")
            return
betting_system()
hrac()