from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.pos_x = 10
        self.pos_y = 10
        self.speed_ball = 0.1

    def move_the_ball(self):
        new_x = self.xcor() + self.pos_x
        new_y = self.ycor() + self.pos_y
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.pos_y *= -1

    def x_bounce(self):
        self.speed_ball *= 0.9
        self.pos_x *= -1

    def reverse_ball(self):
        self.speed_ball = 0.1
        self.x_bounce()
