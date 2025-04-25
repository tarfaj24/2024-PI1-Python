import tkinter as tk
import random

# Inicializácia dát
symbols = ["A", "A", "B", "B", "C", "C", "D", "D",
           "E", "E", "F", "F", "G", "G", "H", "H"]
random.shuffle(symbols)

# Premenné
first = None
second = None
buttons = []
revealed = [False] * 16

# Funkcia na kliknutie na kartu
def on_click(i):
    global first, second

    if revealed[i] or second is not None:
        return  # nič nerob, ak je karta už odhalená alebo čakáme

    buttons[i].config(text=symbols[i], state="disabled")
    if first is None:
        first = i
    else:
        second = i
        if symbols[first] == symbols[second]:
            revealed[first] = True
            revealed[second] = True
            reset_turn()
        else:
            # Po 1 sekunde otočí späť
            root.after(1000, hide_cards)

# Skrytie kariet
def hide_cards():
    global first, second
    buttons[first].config(text="?", state="normal")
    buttons[second].config(text="?", state="normal")
    reset_turn()

# Reset ťahu
def reset_turn():
    global first, second
    first = None
    second = None

# Vytvorenie okna
root = tk.Tk()
root.title("Pexeso")

# Vytvorenie tlačidiel
for i in range(16):
    btn = tk.Button(root, text="?", width=4, height=2,
                    command=lambda i=i: on_click(i), font=("Arial", 24))
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    buttons.append(btn)

root.mainloop()