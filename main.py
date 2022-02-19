from turtle import Screen,Turtle
import time
from snake import Snake

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
screen.onkey(key='Up',fun=Snake.Up)
screen.onkey(key='Down',fun=Snake.Down)
screen.onkey(key="Right",fun=Snake.Right)
screen.onkey(key= 'Left',fun=Snake.Left)
while 1:
    screen.update()
    Snake.snakeForward(SnakeList=SnakeList)
    screen.update()
    time.sleep(0.1)

screen.exitonclick()








screen.exitonclick()