import math
import random
from turtle import Turtle

STARTING_NUMBER_OF_UNITS = 100
X_BOUNDS = (-300, 300)
Y_BOUNDS = (-300, 300)
UNIT_SPEED = 10
TEAM_COLORS = ["green", "blue", "red"] # Rocks, Scissors, Paper
TEAM_SPAWN_ZONES = []

class TeamManager:
    def __init__(self, team):
        super().__init__()
        self.units = []
        self.spawner(team)

    # Add rock
    def add_unit(self, team):
        new_unit = Turtle(shape="turtle")
        new_unit.penup()

        if team == "rock":
            new_unit.color(TEAM_COLORS[0])
        elif team == "scissor":
            new_unit.color(TEAM_COLORS[1])
        else:
            new_unit.color(TEAM_COLORS[2])

        new_unit.goto(random.randint(-325, 325), random.randint(-325, 325))
        self.units.append(new_unit)

    # Generate rocks
    def spawner(self, team):
        for number in range(0, STARTING_NUMBER_OF_UNITS):
            self.add_unit(team)

    # Change direction based on chasing/retreating
    def change_heading(self, mover, target, direction):
        # get positions
        x1, y1 = mover.pos()
        x2, y2 = target.pos()

        # calculate angle
        dx = x2 - x1
        dy = y2 - y1
        angle = math.degrees(math.atan2(dy, dx))

        # turn mover to face away from target
        if direction == -1:
            mover.setheading(-angle)
        # turn mover to face from target
        else:
            mover.setheading(angle)

    # Go forward based on chasing/retreating
    def move(self, mover, target, retreating):
        if retreating:
            self.change_heading(mover, target, -1)
            self.hit_wall(mover)
            mover.forward(UNIT_SPEED)
        else:
            # self.hit_wall(mover)
            self.change_heading(mover, target, 1)
            mover.forward(UNIT_SPEED)

    def capture(self, captured_unit, captured_by, friends, targets):
        captured_unit.color(captured_by.color()[0])
        friends.append(captured_unit)
        targets.remove(captured_unit)

    def hit_wall(self, unit):
        if unit.xcor() > X_BOUNDS[1]:
            unit.setheading(260)
        elif unit.ycor() > Y_BOUNDS[1]:
            unit.setheading(350)
        elif unit.xcor() < X_BOUNDS[0]:
            unit.setheading(80)
        elif unit.ycor() < Y_BOUNDS[0]:
            unit.setheading(170)


    def find_closest(self, unit, friends, enemies, targets):
        closest_enemy_distance = 999
        closest_target_distance = 999
        closest_enemy = None
        closest_target = None

        if len(enemies) > 0:
            for enemy in enemies:
                if unit.distance(enemy) < closest_enemy_distance:
                    closest_enemy_distance = unit.distance(enemy)
                    closest_enemy = enemy
        else:
            closest_enemy = None

        if len(targets) > 0:
            for target in targets:
                if unit.distance(target) < closest_target_distance:
                    closest_target_distance = unit.distance(target)
                    closest_target = targets[targets.index(target)]
                    if unit.distance(closest_target) < 30:
                        self.capture(closest_target, unit, friends, targets)
                        return closest_target
        else:
            closest_target = None

        if closest_enemy is None:
            return closest_target
        elif closest_target is None:
            return closest_enemy
        elif unit.distance(closest_target) <= unit.distance(closest_enemy):
            return closest_target
        else:
            return closest_enemy




