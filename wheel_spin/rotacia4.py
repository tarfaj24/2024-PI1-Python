from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import random
import math
argument_uhol1 =random.randint(0,360)

list_s_moznostami = ['marek', 'fero', 'jano',"samo","smaco","janoslav","fesda","adsaddsadasdasdsd"]
argument_dlzka_inputu = len(list_s_moznostami)

def vypocet_polohy_podla_uhlu(uhol):
    stred_x = 200
    stred_y = 200
    polomer = 200
    r = 0.7
    uhol_rad = math.radians(uhol)
    x = stred_x + math.cos(uhol_rad) * polomer * r
    y = stred_y + math.sin(uhol_rad) * polomer * r
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



def create_hlavna_image(angle,dlzka_inputu,poloha_x,poloha_y):
    
    # Create base canvas (master image)
    hlavna_img = Image.new("RGBA", (400, 400), (255, 255, 255, 200))  # semi-transparent white
    uhol = 0
    uhol1 = 0
    
    for i in range(len(list_s_moznostami)):
        x,y = vypocet_polohy_podla_uhlu(uhol)
        x,y = int(x),int(y)
        img1 = make_label_image(list_s_moznostami[i],font_size=20,color="black",uhol_otocenia=uhol1)
        hlavna_img.paste(img1,(x,y),img1)
        uhol-=360/len(list_s_moznostami)
        uhol1= 200-uhol-20
        print(uhol)
        
        
       
        
    # img1 = make_label_image("Box Aasdsadasd", color="blue",uhol_otocenia=30)
    # img2 = make_label_image("Box B", color="red",uhol_otocenia=90)
    # img3 = make_label_image("Box C", color="green",uhol_otocenia=140)
    

       
    # hlavna_img.paste(img2, (150, 100), img2)
    # hlavna_img.paste(img3, (80, 200), img3)

    # Rotate the whole thing
    rotated = hlavna_img.rotate(angle, expand=True)
    

    return rotated

# Tkinter window
root = tk.Tk()
root.title("Composite Image on Canvas")

# Create final image
final_pil_image = create_hlavna_image(0,argument_dlzka_inputu,20,20)
tk_image = ImageTk.PhotoImage(final_pil_image)

# Tkinter canvas
canvas = tk.Canvas(root, width=400, height=400, bg="lightgray")
canvas.pack()
canvas.create_image(200, 200, image=tk_image)
canvas.image = tk_image  # prevent garbage collection

root.mainloop()