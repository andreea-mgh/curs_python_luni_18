import turtle
# cum prescurtam numele functiilor din pachetele:
from random import randint as rand

turtle.color("SkyBlue4")
turtle.shape("turtle")
turtle.speed(4)

turtle.pendown()

palette = ["pink", "orange", "purple"]


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
def poligon(nr, latura):
    turtle.begin_fill()
    for i in range(nr): # 3 laturi
        turtle.forward(latura)
        turtle.left(360/nr) # 360/3
    turtle.end_fill()


for i in range(30): # repeta de 30 de ori
    turtle.color( palette[rand(0,len(palette)-1)] )
    turtle.penup()
    turtle.goto(rand(-150,150), rand(-100,100))
    turtle.pendown()
    poligon(rand(3,6),rand(20,80))



turtle.done()