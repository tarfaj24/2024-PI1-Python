import tkinter as tk

okno = tk.Tk()
platno = tk.Canvas(okno,width = 400,height = 400,bg = "blue")

tlacidlo1 = tk.Button(okno,text = "Prvé")
tlacidlo1.pack()
tlacidlo1.bind("<Enter>",lambda e: print("Myš je nad tlacidlom 1"))

tlacidlo2 = tk.Button(okno, text="Druhé")
tlacidlo2.pack()
tlacidlo2.bind("<Enter>", lambda e: print("Mys je nad tlacidlom 2"))

tk.mainloop()