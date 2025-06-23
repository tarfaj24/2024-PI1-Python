from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk

root = tk.Tk()

# Create base image
img = Image.new("RGBA", (300, 150), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Load font with larger size
try:
    font = ImageFont.truetype("arial.ttf", 60)
except OSError:
    print("Could not load 'arial.ttf'. Using default font.")
    font = ImageFont.load_default()  # Won’t scale up

# Draw text
draw.text((10, 10), "Hello", font=font, fill="black")

# Rotate image
rotated = img.rotate(45, expand=True)
tk_img = ImageTk.PhotoImage(rotated)

# Display with Tkinter
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_image(200, 200, image=tk_img)

canvas.image = tk_img  # Keep a reference
root.mainloop()