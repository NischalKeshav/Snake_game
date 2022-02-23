
import turtle
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-100,270)
        self.color('White')
        with open("new.txt") as data:
           self.highscore = int(data.read())
      
    def score(self,score):
        self.clear()
        self.scored = score
        if score > self.highscore:
          self.highscore = score
        
          with open("new.txt",mode="w") as x:
              x.write(str(self.highscore))
        self.write(f"Score:{score}    High Score:{self.highscore}",font=('Arial',18,'normal'))
    # def GameOver(self,Cont):
    #     self.goto(-50, 60)
    #     self.write("GAME OVER", font=('Arial', 32, 'normal'))
    #     Cont = False
    def reset(self,score):
          score = 0