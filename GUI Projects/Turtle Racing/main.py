import random
import turtle
from turtle import Turtle, Screen


colors = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
is_race_on = False
x_value = -230
y_value = -100
current_color = 0
all_turtles = []
for turt in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turt])
    current_color += 1
    new_turtle.penup()
    new_turtle.goto(x_value, y_value)
    y_value += 50
    all_turtles.append(new_turtle)

screen = Screen()

user_bet = screen.textinput(title="place your bet ", prompt="which turtle will win the race? Enter a color")

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 320:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won, {winning_color} is the winner")
            else:
                print(f"you've lost, {winning_color} is the winner")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
