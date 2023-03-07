from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 35, "bold")


class ScoreBoard(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.score = 0
        self.color(color)
        self.hideturtle()
        self.penup()
        self.goto(position)

    def update_l_score(self):
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def increase_l_score(self):
        self.score += 1
        self.clear()
        self.update_l_score()

    def update_r_score(self):
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def increase_r_score(self):
        self.score += 1
        self.clear()
        self.update_r_score()

    def game_over_l(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"Game Over !!!, Red wins!!!", align=ALIGN, font=FONT)

    def game_over_r(self):
        self.goto(0, 0)
        self.color("blue")
        self.write(f"Game Over !!!, Blue wins!!!", align=ALIGN, font=FONT)