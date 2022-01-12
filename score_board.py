from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.scores()

    def scores(self):
        self.write(f"{self.score_1} : {self.score_2}", align=ALIGNMENT, font=FONT)

    def increase_score_1(self):
        self.score_2 += 1
        self.clear()
        self.scores()

    def increase_score_2(self):
        self.score_1 += 1
        self.clear()
        self.scores()



