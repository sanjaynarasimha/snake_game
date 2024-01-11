from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0)
        self.color("blue")
        self.refresh()

    def refresh(self):
        x_dir = random.randint(-270, 270)
        y_dir = random.randint(-270, 270)
        self.goto(x_dir, y_dir)

