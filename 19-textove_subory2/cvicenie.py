import random, tkinter
#aa
subor = open("subor_vykreslovanie","w")
canvas = tkinter.Canvas(height = 800, width = 800)
canvas.pack()
width = 800
height = 800
listriadkov = []
for i in range(10):
    riadok = random.choice("ORL") + " " + str(random.randint(3,width-3)) +" "+  str(random.randint(3,height - 3)) +" "+ str(random.randint(3,width-3)) + " "+ str(random.randint(3,height - 3)) + " " + str(random.randint(0,255)) + " "+ str(random.randint(0,255)) + " "+ str(random.randint(0,255))

    print(riadok,file = subor)

    list1 = list(riadok)
    print(listriadkov)
    tvar,x,y,x1,y1,r,g,b = riadok.split()
    x = int(x)
    y = int(y)
    x1 = int(x1)
    y1 = int(y1)
    r = int(r)
    g = int(g)
    b = int(b)
    farba = f'#{r:02x}{g:02x}{b:02x}'

    if list1[0] == "O":
        farba = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_oval(x,y,x1,y1,fill = farba)
    elif list1[0] == "R":
        farba = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_rectangle(x,y,x1,y1,fill = farba)
    elif list1[0] == "L":
        farba = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(x,y,x1,y1,fill = farba)
        



subor.close()
tkinter.mainloop()