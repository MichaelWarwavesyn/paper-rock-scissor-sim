import random
import time
from turtle import Screen, Turtle

from team_manager import TeamManager

FONT = ("Courier", 24, "normal")

# Create the screen
screen = Screen()
screen.setup(width=700, height=700)
screen.tracer(0)
screen.listen()

# Create the teams
rock_team = TeamManager(team="rock")
scissor_team = TeamManager(team="scissor")
paper_team = TeamManager(team="paper")

scoreboard = Turtle()
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 0)


game_is_on = True
while game_is_on:
    time.sleep(0.05)

    if len(paper_team.units) < 0 or len(scissor_team.units) < 0:
        if len(rock_team.units) < 0:
            game_is_on = False
    else:
        if len(rock_team.units) > 0:
            for rock in rock_team.units:
                closest = rock_team.find_closest(unit=rock, friends=rock_team.units, enemies=paper_team.units, targets=scissor_team.units,)
                if closest is not None:
                    if closest.color()[0] == "red":
                        rock_team.move(rock, closest, True)
                    else:
                        rock_team.move(rock, closest, False)

        if len(scissor_team.units) > 0:
            for scissor in scissor_team.units:
                closest = scissor_team.find_closest(unit=scissor, friends=scissor_team.units, enemies=rock_team.units, targets=paper_team.units,)
                if closest is not None:
                    if closest.color()[0] == "green":
                        scissor_team.move(scissor, closest, True)
                    else:
                        scissor_team.move(scissor, closest, False)

        if len(paper_team.units) > 0:
            for paper in paper_team.units:
                closest = paper_team.find_closest(unit=paper, friends=paper_team.units, enemies=scissor_team.units, targets=rock_team.units,)
                if closest is not None:
                    if closest.color()[0] == "blue":
                        paper_team.move(paper, closest, True)
                    else:
                        paper_team.move(paper, closest, False)

    screen.update()

screen.exitonclick()
