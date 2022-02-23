import turtle
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-100,270)
        self.color('White')
        self.highscore=0
    def score(self,score):
        self.clear()
        self.scored = score
        if score > self.highscore:
          self.highscore = score
        self.write(f"Score:{score}    High Score:{self.highscore}",font=('Arial',18,'normal'))
    # def GameOver(self,Cont):
    #     self.goto(-50, 60)
    #     self.write("GAME OVER", font=('Arial', 32, 'normal'))
    #     Cont = False
    def reset(self):
      if self.score > self.highscore:
          self.highscore = self.score
          self.score = 0