from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(x_cor, y_cor)

    # def move_down(self):
    #     x_cor = self.xcor()
    #     y_cor = self.ycor() - MOVE_DISTANCE
    #     self.goto(x_cor, y_cor)
    #
    # def move_right(self):
    #     x_cor = self.xcor() + MOVE_DISTANCE
    #     y_cor = self.ycor()
    #     self.goto(x_cor, y_cor)
    #
    # def move_left(self):
    #     x_cor = self.xcor() - MOVE_DISTANCE
    #     y_cor = self.ycor()
    #     self.goto(x_cor, y_cor)

    def reset_player(self):
        self.goto(STARTING_POSITION)