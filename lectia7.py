import tkinter as tk
from random import randint as rand
from random import choice

FPS = 50


# Clasă: un set de atribute și acțiuni (= metode) care 
#   reprezinta caracteristicile unui obiect.

# clasele se scriu cu litera mare!!
# nu e obligatoriu, dar asa se face :)
class Fish:
    # toate clasele au o functie "constructor"
    # care controleaza cum se creeaza obiectul
    def __init__(self):
        # facem atribute!
        self.color = choice(['coral', 'darkolivegreen1', 'darkseagreen1', 'firebrick1', 'darkorange'])
        self.size = rand(10,30)
        self.x = rand(20,380)
        self.y = rand(20,380)
        self.vx = rand(-50, 50)
        self.vy = rand(-5, 5)
    
    # facem metode!
    def draw(self, canvas):
        # canvas.create_rectangle(self.x - self.size, self.y - self.size/2,
        #                         self.x + self.size, self.y + self.size/2,
        #                         fill=self.color, outline="")
        x = self.x
        y = self.y
        s = self.size

        if self.vx < 0:
            points = [x+s, y,
                      x, y+s/2,
                      x-s, y,
                      x, y-s/2,
                      # coada
                      x+s, y,
                      x+s*1.5, y-s/2,
                      x+s*1.5, y+s/2]
            canvas.create_polygon(points, fill=self.color)
        else:
            # x-s devine x+s
            # x+s devine x-s
            points = [x-s, y,
                      x, y+s/2,
                      x+s, y,
                      x, y-s/2,
                      # coada
                      x-s, y,
                      x-s*1.5, y-s/2,
                      x-s*1.5, y+s/2]
            canvas.create_polygon(points, fill=self.color)


    
    def move(self):
        self.x += self.vx / FPS
        self.y += self.vy / FPS

        if self.x < 0 or self.x > 400:
            self.vx = -self.vx

        if self.y < 0 or self.y > 400:
            self.vy = -self.vy
        
        






fishtank = []
for _ in range(30):
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
    win.after(1000//FPS, update)

update()
win.mainloop()