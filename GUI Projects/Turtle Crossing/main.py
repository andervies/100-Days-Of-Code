from turtle import Screen
from user_turtle import UserTurtle
from car_manager import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)

user_turtle = UserTurtle()
car_manager = Car()
scoreboard = Scoreboard()

screen.tracer(0)
screen.listen()
screen.onkey(user_turtle.move, "Up")


is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(user_turtle) < 20:
            is_game_on = False
            scoreboard.game_over()
    if user_turtle.is_at_finish_line():
        user_turtle.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()

