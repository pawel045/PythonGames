from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):

        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('yellow')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.move_food()

    def move_food(self):

        self.goto(20*randint(-14, 14), 20*randint(-14, 14))

