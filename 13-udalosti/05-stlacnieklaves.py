import tkinter as tk

okno = tk.Tk()
platno = tk.Canvas(okno,width = 400,height = 400,bg = "blue")

def klaves_stlaceny(event):
    print("stlačený",event.keysym)

def klaves_pusteny(event):
    print("pustený",event.keysym)

okno.bind("<KeyPress>",klaves_stlaceny)
okno.bind("<KeyRelease>",klaves_pusteny)


tk.mainloop()