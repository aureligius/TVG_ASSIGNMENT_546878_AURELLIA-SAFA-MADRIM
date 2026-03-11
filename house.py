import tkinter as tk

# create window
window = tk.Tk()
window.title("Geometric Shapes Scene")

# create canvas
canvas = tk.Canvas(window, width=600, height=400, bg="#FFA856")
canvas.pack()

# MOUNTAIN (triangle)
canvas.create_polygon(-20, 300, 200, 100, 400, 300, fill="#01118F", outline="")
canvas.create_polygon(200, 300, 400, 60, 620, 300, fill="#01118F", outline="")

# RUMPUT (rectangle)
canvas.create_rectangle(0,300, 620, 420 , fill = "#3B810C", outline="")

# SUN (circle)
canvas.create_oval(240, 40, 340, 140, fill="#DF7B17", outline="")

# CLOUD (ellipse)
canvas.create_oval(80, 60, 160, 100, fill="white", outline="")
canvas.create_oval(120, 40, 200, 100, fill="white", outline="")
canvas.create_oval(160, 60, 240, 100, fill="white", outline="")

# CLOUD 2 (ellipse)
canvas.create_oval(80, 60, 160, 100, fill="white", outline="")
canvas.create_oval(120, 40, 200, 100, fill="white", outline="")
canvas.create_oval(160, 60, 240, 100, fill="white", outline="")

# HOUSE BODY (rectangle)
canvas.create_rectangle(200, 200, 400, 320, fill="#AC8E86", outline="black")

# ROOF (triangle polygon)
canvas.create_polygon(170, 200, 300, 120, 430, 200, fill="#D79AA3", outline="black")


# DOOR (rectangle)
canvas.create_rectangle(275, 240, 325, 310, fill="#B67C85")

# WINDOW I(hexagon)
canvas.create_polygon(
    220,250,
    240,235,
    260,250,
    260,275,
    240,290,
    220,275,
    fill="#E2CBCF",
    outline="white"
)
canvas.create_polygon(
    340,250,
    360,235,
    380,250,
    380,275,
    360,290,
    340,275,
    fill="#E2CBCF",
    outline="white"
)

window.mainloop()