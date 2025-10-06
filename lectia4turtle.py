import turtle
# cum prescurtam numele functiilor din pachetele:
from random import randint as rand

turtle.color("SkyBlue4")
turtle.shape("turtle")
turtle.speed(4)

turtle.pendown()

def patrat(latura=50):
    for i in range(4): # 4 laturi
        turtle.forward(latura)
        turtle.left(90) # 360/4

def triunghi(latura):
    for i in range(3): # 3 laturi
        turtle.forward(latura)
        turtle.left(120) # 360/3

# ca sa facem un poligon, ne rotim cu
# 360 impartit la numarul de laturi


for i in range(30): # repeta de 30 de ori
    turtle.penup()
    turtle.goto(rand(-150,150), rand(-100,100))
    turtle.pendown()
    triunghi(rand(20,80))



turtle.done()