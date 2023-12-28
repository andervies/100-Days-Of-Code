from turtle import Turtle
import random

list = ["cyan", "turquoise", "blue", "pink", "orange",   "green", "navy"]
tola = Turtle()
for i in range(int(360/5)):
    tola.speed(15)
    tola.color(random.choice(list))
    tola.circle(100)
    tola.right(5)
