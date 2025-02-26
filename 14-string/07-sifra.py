#cézarova sifra ahoj bgpk vzdy sa zvacsi o 1
import tkinter
canvas = tkinter.Canvas(width=600,height = 600)
canvas.pack(side = "left")





def sifra():
    strvstup = vstup.get()
    sifrslovo = ""
    sifcislo = 0
    for pismeno in strvstup:
            sifcislo = (ord(pismeno)+1)
            sifpismeno = chr(sifcislo)
            sifrslovo += sifpismeno
    canvas.create_text(300,200,text = sifrslovo,font= "arial 50")

def odsifrovanie():
    strvstup = vstup.get()
    odsifcislo = 0
    odsifrslovo = ""
    for pismeno1 in strvstup:
            odsifcislo = (ord(pismeno1)-1)
            odsifpismeno = chr(odsifcislo)
            odsifrslovo += odsifpismeno
    canvas.create_text(300,200,text = odsifrslovo,font= "arial 50")

def zmaz():
      canvas.delete("all")


tkinter.Button(text = "Zašifrovať",font = "arial 20", command=sifra,).pack()
tkinter.Button(text = "odsifrovat",font = "arial 20", command=odsifrovanie).pack()
tkinter.Button(text = "zmaz",font = "arial 20", command=zmaz).pack()

tkinter.Label(text = "zadaj text na zašifrovanie",font = "arial 20").pack()
vstup = tkinter.Entry(font = "arial 20")
vstup.pack()

tkinter.mainloop()
