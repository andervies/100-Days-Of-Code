import turtle
import random


colors = ["red", "blue", "aquamarine", "orange", "purple", "violet", "pink", "green", "turquoise", "gold", "silver"]
tola = turtle.Turtle()
for i in range(3, 11):
    angle = round(360 / i)
    tola.color(random.choice(colors))
    for j in range(i):
        tola.forward(100)
        tola.right(angle)
