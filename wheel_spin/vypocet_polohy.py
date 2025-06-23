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

def make_label_image(text, font_size=20, color="black",uhol_otocenia=30):
    font = ImageFont.truetype("arial.ttf", font_size)
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



root = tk.Tk()
platno = tk.Canvas(root,width=400,height=400)
platno.pack()

print(vypocet_polohy_podla_uhlu(170))

tk.mainloop()