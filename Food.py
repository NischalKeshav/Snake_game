from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.75,stretch_wid=.75)
        self.color('Red')
        self.speed("fastest")
        X = random.randint(-14,14)*20
        Y = random.randint(-14, 14) * 20
        self.goto(X,Y)
    def refresh(self):
        X = random.randint(-14, 14) * 20
        Y = random.randint(-14, 14) * 20
        self.goto(X, Y)