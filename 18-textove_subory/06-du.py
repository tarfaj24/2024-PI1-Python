#oval alebo kruh,farba,x,y + test z textovych suborov a polí
import tkinter

canvas = tkinter.Canvas(width= 400, height=400)
canvas.pack()

subor = open("body2.txt","r")

listsuboru = []

for riadok in subor:
    riadok = riadok.strip()
    listsuboru.append(riadok)


cislo2 = 4
print(listsuboru)
#body
for i in range(2,12,3):
    if i == 2 or i == 11:
        body = listsuboru[i]
        medzera = body.find(" ")

        x = int(body[:medzera])
        y = int(body[medzera+1:])
        print(x,y)
        
        farbaovalu = "red"

        canvas.create_oval(x-5,y-5,x+5,y+5,fill=farbaovalu)
        

    if i == 5 or i == 8:
        body = listsuboru[i]
        medzera = body.find(" ")

        x1 = int(body[:medzera])
        y1 = int(body[medzera+1:])
        print(x1,y1)
        farba = listsuboru[cislo2]
        canvas.create_rectangle(x1-5,y1-5,x1+5,y1+5,fill=farba)
        cislo2 += 3






    

tkinter.mainloop()