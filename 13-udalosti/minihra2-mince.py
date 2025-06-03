import tkinter as tk
import random

okno = tk.Tk()
okno.title("zbieranie mincí")
okno.geometry("500x500")

label = tk.Label(okno,text =f"Skóre: 0    Čas: 30",font=("Arial 14"))
label.pack()

platno = tk.Canvas(okno,width = 500, height = 500, bg = "white")
platno.pack()

hrac = platno.create_rectangle(240,240,260,260,fill="blue")

skore = 0
cas = 30



mince = []

def pohyb(event):
    dx,dy = 0,0

    if event.keysym == "Up":
        dy = -10
    elif event.keysym == "Down":
        dy = 10
    elif event.keysym == "Left":
        dx = -10
    elif event.keysym == "Right":
        dx = 10
    platno.move(hrac,dx,dy)
    skontroluj_koliziu()

def klik_na_platno(event):
    x,y = event.x,event.y
    minca = platno.create_oval(x-10,y-10,x+10,y+10)
    mince.append(minca)

def skontroluj_koliziu():
    global skore
    hrac_coords = platno.coords(hrac)
    for minca in mince[:]:
        if kolizia(hrac_coords,platno.coords(minca)):
            platno.delete(minca)
            mince.remove(minca)
            skore+=1
            label.config(text=f"Skóre: {skore}   Čas: {cas}")

def kolizia(obj1,obj2):
    x1,y1,x2,y2 = obj1
    a1,b1,a2,b2 = obj2
    return not(x2<a1 or x1>a2 or y2 < b1 or y1 > b2)

def odpocet():
    global cas
    if cas > 0:
        cas-=1
        label.config(text=f"Skóre: {skore}   Čas: {cas}")
        okno.after(1000,odpocet)
    else:
        platno.unbind("<Button-1")
        okno.unbind("<Key>")
        label.config(text = f"Koniec! Skore: {skore}")

okno.bind("<Key>",pohyb)
platno.bind("<Button-1>",klik_na_platno)

odpocet()



tk.mainloop()

