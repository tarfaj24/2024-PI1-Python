from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import random
import math

# Vstup
mena = input("Zadaj mená oddelené medzerou: ").split()
pocet = len(mena)

# Globálne premenné
uhol = random.randint(0, 360)
rychlost = 10.0
spustene = True

# Tkinter GUI
okno = tk.Tk()
platno = tk.Canvas(okno, width=400, height=400)
platno.pack()

# Výpočet pozície podľa uhla
def vypocitaj_poziciu(uhol_stupne):
    r = 120
    stred = 200
    rad = math.radians(uhol_stupne)
    x = stred + math.cos(rad) * r
    y = stred + math.sin(rad) * r
    return x, y

# Vytvorenie obrázka kolesa
def vytvor_koleso(uhol_otocenia):
    img = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Font
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()

    # Kreslenie sektorov
    for i in range(pocet):
        start = uhol_otocenia + i * (360 / pocet)
        farba = (200 + i*20) % 255
        draw.pieslice((10, 10, 390, 390), start=start, end=start + 360/pocet, fill=(farba, 100, 200))

    # Pridanie mien
    for i in range(pocet):
        uhol_mena = uhol_otocenia + i * (360 / pocet) + (360 / pocet) / 2
        x, y = vypocitaj_poziciu(uhol_mena)

        bbox = draw.textbbox((0, 0), mena[i], font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]

        draw.text((x - w/2, y - h/2), mena[i], fill="black", font=font)

    return img

# Animácia
def animuj():
    global uhol, rychlost, spustene

    platno.delete("all")

    if spustene:
        img = vytvor_koleso(uhol)
        tk_img = ImageTk.PhotoImage(img)
        platno.create_image(200, 200, image=tk_img)
        platno.image = tk_img

        uhol += rychlost
        uhol %= 360

        if rychlost > 0.1:
            rychlost *= 0.97
        else:
            spustene = False

        platno.after(30, animuj)

# Spusti animáciu
animuj()
okno.mainloop()