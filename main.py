import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
level = 1
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()
screen.onkey(fun=player.move_up, key="Up")
# screen.onkey(fun=player.move_down, key="Down")
# screen.onkey(fun=player.move_right, key="Right")
# screen.onkey(fun=player.move_left, key="Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move()
    if player.ycor() >= 290:
        player.reset_player()
        level += 1
        scoreboard.add_level(level)
        car_manager.add_speed()
    else:
        for car in car_manager.cars:
            if player.distance(car) < 20:
                scoreboard.game_over(level)
                game_is_on = False
    screen.update()

screen.exitonclick()
