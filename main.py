from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Ping-Pong-Ball")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


r_paddle = Paddle((350,0), "blue")
l_paddle = Paddle((-350,0), "red")

ball = Ball()

scoreboard_l = ScoreBoard((35,220), "blue")
scoreboard_r = ScoreBoard((-35,220), "red")


scoreboard = ScoreBoard((0,0), "white")
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        if ball.distance(r_paddle) < 25 or ball.distance(l_paddle) < 25:
            ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard_r.increase_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard_l.increase_r_score()

    if scoreboard_l.score == 11 :
        scoreboard.game_over_r()
        is_game_on = False
    elif scoreboard_r.score == 11:
        scoreboard.game_over_l()
        is_game_on = False















screen.exitonclick()
