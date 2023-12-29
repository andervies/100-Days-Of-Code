from turtle import Turtle

STARTING_POSITION = (0, -200)
FINISH_LINE_Y = 280
MOVE_DISTANCE = 10


class UserTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.setposition(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False





