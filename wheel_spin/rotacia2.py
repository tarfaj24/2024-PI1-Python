from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk

root = tk.Tk()


# Create base image
img = Image.new("RGBA", (200, 200), (255, 255, 255, 200))
draw = ImageDraw.Draw(img)

# Draw text
font = ImageFont.truetype("arial.ttf", 15)
draw.text((130, 30), "Hello", font=font, fill="black")

# Rotate and convert
rotated = img.rotate(0, expand=True)
tk_img = ImageTk.PhotoImage(rotated)

# Tkinter display
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_image(200, 200, image=tk_img)

# Keep image reference
canvas.image = tk_img

root.mainloop()