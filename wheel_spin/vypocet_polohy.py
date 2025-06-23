import tkinter as tk
import math

def vypocet_polohy_podla_uhlu(uhol):
    platno.create_oval(10,10,390,390)
    
    stred_x = 200
    stred_y = 200
    polomer = 200
    r = 0.9
    uhol_rad = math.radians(uhol)
    x = stred_x + math.cos(uhol_rad) * polomer * r
    y = stred_y + math.sin(uhol_rad) * polomer * r
    platno.create_rectangle(x,y,x+10,y+10)
    
    return x,y


root = tk.Tk()
platno = tk.Canvas(root,width=400,height=400)
platno.pack()

print(vypocet_polohy_podla_uhlu(170))

tk.mainloop()