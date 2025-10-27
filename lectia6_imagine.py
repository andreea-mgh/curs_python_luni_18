import tkinter as tk

win = tk.Tk()

canvas = tk.Canvas(win, width=400, height=400, background="darkgreen")
canvas.pack()


sprite_x = 100
sprite_y = 100
img = tk.PhotoImage(file="sprite1.png")

def display_sprite(x, y):
    canvas.delete('all')
    canvas.create_image(x, y, image=img)

display_sprite(sprite_x,sprite_y)

# cand legam o functie de un key sau button press,
# functia trebuie sa aiba un parametru "event"
# in care retine ce buton sau tasta s-a apasat
def move_image(event):
    global sprite_x, sprite_y

    if event.keysym == "Up":
        sprite_y -= 10
    
    if event.keysym == "Down":
        sprite_y += 10
    
    if event.keysym == "Left":
        sprite_x -= 10
    
    if event.keysym == "Right":
        sprite_x += 10
    
    display_sprite(sprite_x, sprite_y)



# tasta sus
win.bind("<Up>", move_image)
win.bind("<Down>", move_image)
win.bind("<Left>", move_image)
win.bind("<Right>", move_image)

win.mainloop()