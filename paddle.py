from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates, color):
        super().__init__()
    # paddle = Turtle()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(coordinates)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)