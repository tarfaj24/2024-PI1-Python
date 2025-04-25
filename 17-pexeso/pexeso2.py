import random
import time

def init_game():
    cards = ["a", "a", "b", "b", "c", "c", "d", "d", "e", "e", "f", "f", "g", "g", "h", "h"]
    random.shuffle(cards)
    board = []
    for i in range(0, len(cards), 4):
        board.append(cards[i:i+4])
    return board

def display_board(board, revealed):
    print("   0 1 2 3")
    for row in range(4):
        row_display = f"{row}  "
        for col in range(4):
            if revealed[row][col]:
                row_display += f"{board[row][col]} "
            else:
                row_display += "- "
        print(row_display)
    print()

def player_turn(revealed, message="Zadajte súradnice (riadok stĺpec): "):
    while True:
        user_input = input(message)
        try:
            x, y = map(int, user_input.split())
        except ValueError:
            print("Zadajte dve čísla oddelené medzerou.")
            continue

        if not (0 <= x < 4 and 0 <= y < 4):
            print("Súradnice musia byť v rozsahu 0-3.")
            continue

        if revealed[x][y]:
            print("Táto karta je už otočená.")
            continue

        return x, y

def play_game():
    board = init_game()
    revealed = []
    for i in range(4):
        row = [False, False, False, False]
        revealed.append(row)   
    pairs_left = 8
    turns = 0

    print("🃏 Vitajte v hre PEXESO!")
    display_board(board, revealed)

    while pairs_left > 0:
        print(f"Zostáva párov: {pairs_left}")
        print("Otočte dve karty.")

        x1, y1 = player_turn(revealed, "Prvá karta (riadok stĺpec): ")
        revealed[x1][y1] = True
        display_board(board, revealed)

        while True:
            x2, y2 = player_turn(revealed, "Druhá karta (riadok stĺpec): ")
            if (x2, y2) != (x1, y1):
                break
            print("Nemôžete vybrať tú istú kartu dvakrát.")

        revealed[x2][y2] = True
        display_board(board, revealed)

        if board[x1][y1] == board[x2][y2]:
            print("🎉 Pár sa zhoduje!")
            pairs_left -= 1
        else:
            print("❌ Pár sa nezhoduje. Otočíme ich späť...")
            time.sleep(2)
            revealed[x1][y1] = False
            revealed[x2][y2] = False

        turns += 1
        print(f"Počet ťahov: {turns}\n")

    print("🎊 Gratulujeme! Našli ste všetky páry.")
    print(f"Dokončili ste hru za {turns} ťahov.")

    if input("Chcete hrať znova? (áno/nie): ").strip().lower() == "áno":
        play_game()
    else:
        print("Ďakujeme za hru!")

# Spustenie hry
if __name__ == "__main__":
    play_game()
