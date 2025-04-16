import random
def init_game():
    cards = ["a","a","b","b","c","c","d","d","a","a","b","b","c","c","d","d"]
    random.shuffle(cards)
    board = [cards[i:i+4] for i in range(0, len(cards), 4)]
    return board

def display_board(board, revealed):
    for row in range(4):
        row_display = ""
        for col in range(4):
            if revealed[row][col]:
                row_display += f"{board[row][col]} "
            else:
                row_display += "- "
        print(row_display)
    print()

def player_turn():
    while True:
        try:
            x, y = map(int, input("Zadajte súradnice (riadok, stĺpec): ").split())
            if 0 <= x < 4 and 0 <= y < 4:
                return x, y
            else:
                print("Súradnice musia byť v rozsahu 0-3. Skúste to znova.")
        except ValueError:
            print("Neplatný formát, skúste to znova.")

def play_game():
    board = init_game()  # Inicializujeme hernú plochu
    revealed = [[False]*4 for _ in range(4)]  # Sledovanie odhalených kariet
    pairs_left = 8  # Počet párov, ktoré ešte treba nájsť
    turns = 0  # Počet ťahov

    print("Hra začína!")
    display_board(board, revealed)

    while pairs_left > 0:
        print(f"Zostáva párov: {pairs_left}")
        # Hráč zadá dve rôzne karty, ktoré chce otočiť
        print("Otočte dve karty.")
        x1, y1 = player_turn()
        revealed[x1][y1] = True
        display_board(board, revealed)

        x2, y2 = player_turn()
        revealed[x2][y2] = True
        display_board(board, revealed)

        # Kontrola, či sa karty zhodujú
        if board[x1][y1] == board[x2][y2]:
            print("Pár sa zhoduje!")
            pairs_left -= 1
        else:
            print("Pár sa nezhoduje, otočíme ich späť.")
            revealed[x1][y1] = False
            revealed[x2][y2] = False

        turns += 1
        print(f"Počet ťahov: {turns}\n")
    
    print("Gratulujeme! Vyhrali ste hru.")
    print(f"Počet ťahov: {turns}")

# Spustenie hry
if __name__ == "__main__":
    play_game()