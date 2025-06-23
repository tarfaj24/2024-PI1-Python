from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import random
import math


argument_uhol1 =random.randint(0,360)

argument_spustene = True

input = input("vypis mena: ")
inputsplitnuty = input.split()

print(inputsplitnuty)

dlzkainputu_premenna = len(inputsplitnuty)


argument_spomalovacia_premenna1 = 13.0
spomalovacia_premenna = 7.0

zvacsovanie_premenna = 360/dlzkainputu_premenna
pocet_vykresleni_premenna = 0

argument_uhol_na_pismeno = 0
argument_uhol_na_pismeno1 = 0

def vypocet_polohy_podla_uhlu(uhol):
    stred_x = 180
    stred_y = 180
    polomer = 200
    r = 0.6
    uhol_rad = math.radians(uhol)
    x = stred_x + math.cos(uhol_rad) * polomer * r
    y = stred_y + math.sin(uhol_rad) * polomer * r
    return x,y

def make_label_image(text, font_size=20, color="black",uhol_otocenia=30):
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except OSError:
        font = ImageFont.load_default()
    # na meranie velkosti
    skusobna_img = Image.new("RGBA", (1, 1))
    draw = ImageDraw.Draw(skusobna_img)
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    img = Image.new("RGBA", (w + 8, h + 20), (0, 0, 0, 200))
    draw = ImageDraw.Draw(img)
    draw.text((5, 5), text, font=font, fill=color)
    img1 = img.rotate(uhol_otocenia,expand=True)
    return img1


def create_hlavna_image(uhol,uhol1,dlzka_inputu,x,y):
    
    # Create base canvas (master image)
    hlavna_img = Image.new("RGBA", (400, 400), (255, 255, 255, 200))  # semi-transparent white
    uhol = 0
    uhol1 = 0
    
    for i in range(dlzka_inputu):
        x,y = vypocet_polohy_podla_uhlu(uhol)
        x,y = int(x),int(y)
        img1 = make_label_image(inputsplitnuty[i],font_size=20,color="black",uhol_otocenia=uhol1)
        hlavna_img.paste(img1,(x,y),img1)
        uhol-=360/len(inputsplitnuty)
        uhol1= 200-uhol-20
        print(uhol)
        rotated = hlavna_img.rotate(uhol, expand=True)
    return rotated

def _delete_():
    platno.delete("all")

def tick(sekunda):
    sekunda+=1

def koleso(uhol,zvacsovanie,dlzkainputu,spomalovacia_premenna1,spomalovacia_premenna,spustene,pocet_vykresleni,uhol_na_pismeno,uhol_na_pismeno1):

    if spustene == True:
        _delete_()
        platno.after(16,lambda: koleso(uhol,zvacsovanie,dlzkainputu,spomalovacia_premenna1,spomalovacia_premenna,spustene,pocet_vykresleni,uhol_na_pismeno,uhol_na_pismeno1))
        zvacsovanie=0
        for i in range(dlzkainputu):
            platno.create_arc(10,10,390,390,start = zvacsovanie + uhol,extent = 360/dlzkainputu)
            zvacsovanie+=360/dlzkainputu
        pocet_vykresleni+=1

        final_pil_image = create_hlavna_image(uhol_na_pismeno,uhol_na_pismeno1,dlzkainputu,20,20)
        tk_image = ImageTk.PhotoImage(final_pil_image)
        platno.create_image(200, 200, image=tk_image)
        platno.image = tk_image  
        uhol_na_pismeno+=1

        #print(pocet_vykresleni)
        
        #print(rychlost_kolesa)
        # if pocet_vykresleni>100:
        #     uhol-=50
        
        if pocet_vykresleni>100:
            spomalovacia_premenna-=0.025
            uhol+=spomalovacia_premenna

            
            if spomalovacia_premenna < 1:
                 spustene = False
            if uhol < 1:
                spustene = False
        else:
            spomalovacia_premenna1-=0.02
            uhol+=spomalovacia_premenna1

        


    


okno = tk.Tk()
platno = tk.Canvas(okno,height = 400,width = 400)
platno.pack()



koleso(argument_uhol1,zvacsovanie_premenna,dlzkainputu_premenna,argument_spomalovacia_premenna1,spomalovacia_premenna,argument_spustene,pocet_vykresleni_premenna,argument_uhol_na_pismeno,argument_uhol_na_pismeno1)




tk.mainloop()