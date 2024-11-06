import tkinter

canvas = tkinter.Canvas()   #vytvorenie plátna a jeho priradenie do premennej Canvas
canvas.pack()   #umiestnenie plátna do okna

canvas.create_text(100, 75, text = "Ahoj") # 100,100 sú súradnice (x = 100, y = 100)
#súradnice zadávame vždy v poradí x, y
# x rastie smerom doprava
# y raste smerom dole
canvas.create_rectangle(50, 50, 150, 100) # vylreslenie štvorca(obdĺžnika)
# prvé dve čísla určujú pozíciu počiatočného bodu
# ďalšie dve určujú pozíciu koncového bodu
canvas.create_oval(50,50,150,100) #vykreslenie oválu(kruhu)
# prvé dve čísla určujú pozíciu počiatočného bodu
# ďalšie dve určujú pozíciu koncového bodu
    # aby zostalo okno otvorené(aby sa nezavrelo
canvas.mainloop()