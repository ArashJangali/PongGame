#(Classes)

#paddle - shape, key movements

#ball - shape, movement, when closes distance on paddle, moves randomly in the other direction, if ball touches end of screen, game over


#Score board - shape and size, points

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


paddle_1 = Paddle(-350)


paddle_2 = Paddle(350)

ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(paddle_1.Up, key="Up")
screen.onkey(paddle_1.Down, key="Down")

screen.onkey(paddle_2.Up, key="w")
screen.onkey(paddle_2.Down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 320:
        ball.setx(320)
        ball.bounce_x()

    if ball.distance(paddle_1) < 50 and ball.xcor() < -320:
        ball.setx(-320)
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()
        scoreboard.r_point()



screen.exitonclick()