import tkinter as tk

okno = tk.Tk()
platno = tk.Canvas(okno,height = 400,width = 400)
platno.pack()

# platno.create_arc(100,100,300,300)
platno.create_arc(100,100,300,300,start = 0)
platno.create_arc(100,100,300,300,start = 90)
platno.create_arc(100,100,300,300,start = 180)
platno.create_arc(100,100,300,300,start = 270)


tk.mainloop()