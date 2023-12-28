import turtle

import another_file
from prettytable import PrettyTable
print(another_file.another_variable)
from turtle import Turtle,Screen
rapofly = Turtle()

my_screen = Screen()
rapofly.shape("turtle")
rapofly.color("coral")
rapofly.forward(distance=100)
print(my_screen.canvheight)
my_screen.exitonclick()
table = PrettyTable()
print(table)
table.add_column("Pokemon Name", ["Pikachu", "squirtle", "charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "r"
print(table)