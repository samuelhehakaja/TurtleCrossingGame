from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT2 = ("Courier", 50, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.add_level(1)

    def add_level(self, level):
        self.clear()
        self.write(f"Level: {level}", font=FONT)

    def game_over(self, level):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT2)
        self.goto(0, -25)
        self.write(f"Level: {level}", align="center", font=FONT)
