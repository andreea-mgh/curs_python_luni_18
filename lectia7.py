import tkinter as tk
from random import randint as rand

# Clasă: un set de atribute și acțiuni (= metode) care 
#   reprezinta caracteristicile unui obiect.

# clasele se scriu cu litera mare!!
# nu e obligatoriu, dar asa se face :)
class Fish:
    # toate clasele au o functie "constructor"
    # care controleaza cum se creeaza obiectul
    def __init__(self):
        # facem atribute!
        self.color = "orange"
        self.size = rand(10,30)
        self.x = rand(20,380)
        self.y = rand(20,380)
        self.vx = rand(-30, 30)
        self.vy = rand(-10, 10)
    
    # facem metode!
    def draw(self, canvas):
        canvas.create_rectangle(self.x - self.size, self.y - self.size/2,
                                self.x + self.size, self.y + self.size/2,
                                fill=self.color, outline="")
    
    def move(self):
        self.x += self.vx
        self.y += self.vy





fishtank = []
for _ in range(10):
    fishtank.append(Fish())

win = tk.Tk()

canvas = tk.Canvas(win, width=400, height=400, background='lightblue3')
canvas.pack()

def update():
    canvas.delete('all')
    for fish in fishtank:
        fish.move()
        fish.draw(canvas)
    # after programeaza o functie sa ruleze dupa cateva milisecunde
    # => dupa ce se ruleaza functia update, ruleaza din nou update dupa 20 ms
    win.after(20, update)

update()
win.mainloop()