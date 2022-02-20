import turtle
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-100,270)
        self.color('White')
    def score(self,score):
        self.clear()
        self.write(f"Score:{score}",font=('Arial',18,'normal'))
    def GameOver(self,Cont):
        self.goto(-50, 60)
        self.write("GAME OVER", font=('Arial', 32, 'normal'))
        Cont = False