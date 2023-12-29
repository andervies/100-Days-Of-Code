# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)
import turtle as t
import random

color_list = [(248, 249, 252), (251, 247, 236), (252, 246, 250), (244, 251, 248), (153, 77, 50), (203, 149, 109), (22, 27, 55), (236, 225, 91), (133, 161, 205), (63, 88, 136)]
t.colormode(255)
tola = t.Turtle()

tola.penup()
tola.setheading(225)
tola.forward(300)
tola.setheading(0)
for m in range(10):
    for n in range(10):
        tola.dot(20, random.choice(color_list))
        tola.penup()
        tola.forward(50)
    tola.setheading(90)
    tola.forward(50)



screen = t.Screen()
screen.exitonclick()





