import random, time

def initgame():
    cards = ["a","a","b","b","c","c","d","d","e","e","f","f","g","g","h","h"]
    random.shuffle(cards)
    board = []
    for i in range(0,len(cards),4):
        board.append(cards[i:i+4])
    
    return board

def hraciaplocha(board, otocene):
    print("   0 1 2 3")
    for riadok in range(4):
        spravariadku = f"{riadok} "
        for stlpec in range(4):
            if otocene[riadok][stlpec]:
                spravariadku += f" {board[riadok][stlpec]}"
            else:
                spravariadku += " -"
        print(spravariadku)
    print()

def hracnarade(otocene,sprava="Zadajte súradnice (riadok stĺpec): "):
    while True:
        input_hraca = input(f"{sprava} " )

        try:
            x, y = map(int,input_hraca.split())
        except ValueError:
            print("zadane cisla musia byt oddelene medzerou")
            continue

        if not (0 <= x < 4 and 0 <= y < 4):
            print("zadane cisla musia byt v rozsahu od 0 do 3")
            continue
        if otocene[x][y]:
            print("tato karta uz bola otocena")
            continue
        return x,y

def hra():
    
    print("hra sa zacina")
    
    board = initgame()
    otocene = []
    for i in range(4):
        riadok1 = [False,False,False,False]
        otocene.append(riadok1)

    zostavajucepary = 8
    tahy = 0

    hraciaplocha(board,otocene)

    while zostavajucepary > 0:
        print(f"zostava {zostavajucepary}")
        print("otoc 2 karty")
        x1,y1 = hracnarade(otocene,sprava="zadaj poziciu prvej karty")
        otocene[x1][y1]= True
        hraciaplocha(board,otocene)
        while True:
            x2,y2 = hracnarade(otocene,sprava="zadaj poziciu druhej karty")
            if (x1,y1) != (x2,y2):
                break
            print("tuto kartu si uz otocil")
        otocene[x2][y2]= True
        hraciaplocha(board,otocene)

        if board[x1][y1] == board[x2][y2]:
            print("Spraaavne")
            zostavajucepary -= 1
        else:
            print("❌ Pár sa nezhoduje. Otočíme ich späť...")
            time.sleep(2)
            otocene[x1][y1] = False
            otocene[x2][y2] = False

        tahy += 1
        print(f"Počet ťahov: {tahy}\n")
    print(f"koniec pexesa, dokoncil si ho za {tahy} tahov")
    print("Ďakujeme za hru!")


if __name__ == "__main__":
    hra()

            
            


