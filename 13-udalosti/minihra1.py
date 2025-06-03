import tkinter as tk,random
pocetzmien = 0
pocetkliknuti = 0
pocetkliknuti_pred = 0
cas = 1000


def klik(event): 
    global pocetkliknuti
    pocetkliknuti +=1
   


    
def posun():
    global pocetkliknuti
    global pocetkliknuti_pred
    global cas

    if pocetkliknuti_pred+1 == pocetkliknuti:
        tlacidlo.destroy()
        label1 = tk.Label(text = f"tvoj počet bodov je:{pocetkliknuti}",font=("Arial", 18))
        label1.pack(pady = 200)
    if pocetkliknuti -2 > pocetkliknuti_pred: 
        tlacidlo.destroy()
        label1 = tk.Label(text = "Na tlačidlo nesmieš kliknúť viac krát!!!",font=("Arial", 18))
        label1.pack(pady = 200)
    
    x1 = random.randint(1,720)
    y1 = random.randint(1,720)

    tlacidlo.place(x=x1,y=y1,height = 80,width = 80)
    tlacidlo.after(cas,posun)
    cas = max(100, cas - 10)
    tlacidlo.config(text = f"{pocetkliknuti}")
    pocetkliknuti_pred = pocetkliknuti - 1
    
    

def klik_mimo_tlacidla(event):
    if str(event.widget) == ".":
        tlacidlo.destroy()
        label1 = tk.Label(text = f"tvoj počet bodov je:{pocetkliknuti}",font=("Arial", 18))
        label1.pack(pady = 200)
    
       

    

okno = tk.Tk()
okno.geometry("800x800")

tlacidlo = tk.Button(okno,text = "klikni ma",bg = "red",font="arial 18")



tlacidlo.bind("<Button-1>",klik)
okno.bind("<Button-1>",klik_mimo_tlacidla)


tlacidlo.after(1000,posun)
    



tk.mainloop()