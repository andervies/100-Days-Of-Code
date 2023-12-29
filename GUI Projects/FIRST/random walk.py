import random, turtle


tola = turtle.Turtle()
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)





turtle.colormode(255)
tola.pensize(2)
tola.speed("fastest")

# for i in range(200):
#     tola.color(random_color())
#     tola.forward(20)
#     tola.setheading(random.choice(directions))




for i in range (int(360/5)):
    tola.color(random_color())
    tola.circle(100)
    tola.right(5)

screen = turtle.Screen()
screen.exitonclick()

