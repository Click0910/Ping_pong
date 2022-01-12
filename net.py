from turtle import Turtle


class Net:

    def __init__(self, pos):
        for line_pos in range(0, 10):
            pos[1] -= 50
            line = Turtle(shape="square")
            line.color("white")
            line.resizemode("user")
            line.shapesize(stretch_wid=0.5, stretch_len=2)
            line.setheading(90)
            line.penup()
            line.goto(pos)
            line.speed("fastest")
            # self.line = line
