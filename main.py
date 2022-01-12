from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time
from net import Net

screen = Screen()
screen.bgcolor("black")
screen.setup(width=950, height=600)
screen.tracer(0)

# net = Net([0, 300])
score_board = ScoreBoard()
ping_pong_ball = Ball()
paddle_1 = Paddle((430, 0))
paddle_2 = Paddle((-430, 0))


screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")


def ping_pong_game():

    game_is_on = True

    while game_is_on:
        time.sleep(ping_pong_ball.speed_ball)
        screen.update()
        ping_pong_ball.move_the_ball()

        #Detection collision with wall
        if ping_pong_ball.ycor() > 280 or ping_pong_ball.ycor() < -280:
            ping_pong_ball.y_bounce()

        #Detecting collision with paddle
        if ping_pong_ball.distance(paddle_1) < 50 and ping_pong_ball.xcor() > 400 or \
                ping_pong_ball.distance(paddle_2) < 50 and ping_pong_ball.xcor() < - 400:
                ping_pong_ball.x_bounce()

        #Detecting when the ball goes outside

        if ping_pong_ball.xcor() > 450:
            ping_pong_ball.home()
            time.sleep(1)
            ping_pong_ball.reverse_ball()
            score_board.increase_score_2()

        elif ping_pong_ball.xcor() < -450:
            ping_pong_ball.home()
            time.sleep(1)
            ping_pong_ball.reverse_ball()
            score_board.increase_score_1()


ping_pong_game()


screen.exitonclick()
