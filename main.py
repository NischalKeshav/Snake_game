from turtle import Screen
import time
import turtle
from snake import Snake
from Food import Food
from ScoreBoard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
SnakeList= []
SnakeLength = 3
screen.tracer(0)
Snake = Snake()
Snake.start()
screen.listen()
food = Food()
Score_keep = Scoreboard()
score = 0
screen.onkey(key='Up',fun=Snake.Up)
screen.onkey(key='Down',fun=Snake.Down)
screen.onkey(key="Right",fun=Snake.Right)
screen.onkey(key= 'Left',fun=Snake.Left)
Score_keep.score(score)
Cont= True
while Cont:
    screen.update()
    Snake.snakeForward(SnakeList=SnakeList)
    screen.update()
    time.sleep(0.1)
    #collide with food
    if Snake.SnakeList[0].distance(food)<=20:
        food.refresh()
        score += 1
        Score_keep.score(score)
        Snake.extend()
    try:
        if (Snake.X>290.0 and Snake.heading()==0.0) or (Snake.X < -290.0 and Snake.heading() == 180.0) or  (Snake.Y < -290.0 and Snake.heading() == 270.0) or (Snake.Y > 290.0 and Snake.heading() == 90.0):
            pass
    except:
        Score_keep.GameOver(Cont)
        Cont = False
    Head = Snake.SnakeList[0]
    for x in Snake.SnakeList[1:]:
        if Head.distance(x)<10:
            Score_keep.GameOver(Cont)
            Cont = False

screen.exitonclick()








screen.exitonclick()