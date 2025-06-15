import tkinter as tk

uhol =20

def _delete_():
    platno.delete("all")


def koleso():
    global uhol
    _delete_()
    platno.after(100,koleso)
    platno.create_arc(100,100,300,300,start = 20+uhol)
    platno.create_arc(100,100,300,300,start = 110+uhol)
    platno.create_arc(100,100,300,300,start = 200+uhol)
    platno.create_arc(100,100,300,300,start = 290+uhol)
    uhol+=20
    

    
    

okno = tk.Tk()
platno = tk.Canvas(okno,height = 400,width = 400)
platno.pack()


koleso()
    




tk.mainloop()