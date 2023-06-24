from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, initial_x):
        super().__init__()
        self.setheading(90)

        self.shape("square")
        self.speed("fastest")
        self.color("red")
        self.penup()
        self.shapesize(1, 5)
        self.goto(x=initial_x, y=0)



    def Up(self):
        self.speed("fastest")
        self.setheading(90)
        self.forward(20)

    def Down(self):
        self.speed("fastest")
        self.setheading(270)
        self.forward(20)