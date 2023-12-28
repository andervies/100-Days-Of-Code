from turtle import Turtle
import random as rando

turtle = Turtle()
list = ["cyan", "turquoise", "blue", "pink", "orange",   "green", "navy"]

for i in range(3, 13):
    deg = 360/i
    turtle.color(rando.choice(list))
    for i in range(0, i):
        turtle.forward(100)
        turtle.right(deg)


