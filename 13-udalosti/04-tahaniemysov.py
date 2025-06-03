import tkinter as tk

def tahaj(event):
    platno.coords(kruh,event.x - 25,event.y - 25,event.x + 25,event.y + 25)

okno = tk.Tk()

platno = tk.Canvas(okno,width = 400,height = 300,bg = "white")
platno.pack()

kruh = platno.create_oval(100,100,150,150,fill="blue")

platno.bind("<B1-Motion>",tahaj)

tk.mainloop()