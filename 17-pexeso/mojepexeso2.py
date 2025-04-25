import random, time

def initgame():
    karty = ["a","a","b","b","c","c","d","d","e","e","f","f","g","g","h","h"]
    random.shuffle(karty)
    board = []
    for i in range(0,len(karty),4):
        board.append(karty[i:i+4])
    print(board)
    return board

def hraciaplocha(board,otocene):
    print("  0 1 2 3")
    for riadok in range(4):
        spravariadku = (f"{riadok} ")
        for stlpec in range(4):
            if otocene[riadok][stlpec]:
                spravariadku += (f"{board[riadok][stlpec]} ")
            else:
                spravariadku += "- " 
        print(spravariadku)
def hracnarade(otocene,sprava = "otoc 2 karty(riadok,stlpec)"):
    while True:
        hrac_input = input(f"{sprava} ").strip().lower()
        try:
            x,y = map(int,hrac_input.split())

        except ValueError:
            print("Cisla musia byt oddelene medzerou")
            continue

        if not (0 <= x < 4 and 0 <= y < 4):
            print("cisla musia byt v rozmedzi od 1 do 3")
            continue
        if otocene[x][y]:
            print("tato karta uz bola otocena")
            continue
            
        return x,y
    

def hra():
    board = initgame()
    print("hra sa zacina")
    otocene = []
    for i in range(4):
        riadok1 = [False,False,False,False]
        otocene.append(riadok1)
    
    
    zostavajucepary = 8
    pocettahov = 0

    while zostavajucepary > 0:

        hraciaplocha(board,otocene)
        print(f"pocet tahov = {pocettahov}")
    
        x1,y1 = hracnarade(otocene,"otoc 1 kartu")

        otocene[x1][y1]= True
        hraciaplocha(board,otocene)

        x2,y2 = hracnarade(otocene,"otoc 2 kartu")
        otocene[x2][y2]= True
        hraciaplocha(board,otocene)
        pocettahov+=1
        if board[x1][y1] == board[x2][y2]:
            print("spravne")
            zostavajucepary -= 1
            print(f"zostava {zostavajucepary} párov ")
            time.sleep(2)
        else:
            print("nespravne")
            time.sleep(2)
            otocene[x1][y1] = False
            otocene[x2][y2] = False
            
    print(f"koniec hry,hru si dokoncil za {pocettahov} tahov dakujem za hranie")
            

    

        
    

        



hra()
