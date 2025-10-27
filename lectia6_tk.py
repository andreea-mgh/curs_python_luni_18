import tkinter as tk
from random import randint as rand

def chestie():
    print("ai apasat butonul")

def add_shape():
    x = rand(0,400)
    y = rand(0,400)
    w = rand(50,150)
    h = rand(20,50)
    canvas.create_oval(x, y, x+w, y+h, fill="white", outline="")

# facem un obiect fereastra, il numim "win"
win = tk.Tk()
# facem un obiect buton, il numim "button"
# il cream cu atributele:
#    textul de pe buton "click me"
#    comanda "chestie"
button = tk.Button(win, text="click me", command=chestie)
# afiseaza butonul pe fereastra
button.pack()

buton2 = tk.Button(win, text="adauga obiect", command=add_shape)
buton2.pack()

# https://www.plus2net.com/python/tkinter-colors.php
canvas = tk.Canvas(win, width=400, height=400, bg="lightblue")
canvas.pack()

win.mainloop()


# Toate functiile au paranteze dupa nume.

# Cand cream un obiect, si acolo punem paranteze
# dupa numele obiectului

# Rolul parantezelor e sa transmitem informatii catre
# chestia dupa care punem paranteze.
#    ex. la functii transmitem parametri
#        la obiecte transmitem trasaturile obiectelor

# functiile sunt cu litere mici
# obiectele cu litere mari