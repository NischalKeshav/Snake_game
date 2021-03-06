from turtle import Turtle
class Snake:
    def __init__(self):

        self.SnakeList= []
        self.SnakeList= []
        self.SnakeLength = 3


    def start(self):
        for i in range(4):
            self.T = Turtle()
            self.T.penup()
            self.T.width(2)
            self.T.goto(0 - (20 * i), 0)
            self.T.shapesize(stretch_len=.85,stretch_wid=.85)
            self.T.color('white')
            self.T.shape('square')
            self.SnakeList.append(self.T)
        self.SnakeList[0].setheading(0)    
        self.SnakeList[0].shape('classic')
        self.SnakeList[0].shapesize(stretch_len=1.5,stretch_wid=1.5)
    def add_seg(self,pos):
        self.T = Turtle()
        self.T.penup()
        self.T.goto(pos)
        self.T.shapesize(stretch_len=.85, stretch_wid=.85)
        self.T.color('white')
        self.T.shape('square')
        self.SnakeList.append(self.T)
    def extend(self):
        self.add_seg(self.SnakeList[-1].position())
      


    def new_match(self):
      for i in self.SnakeList:
        i.goto (1000,1000)
      self.SnakeList.clear()
      self.start()
    def Up(self):
        print('up')
        if self.SnakeList[0].heading() == 270:
            return
        else:
            self.SnakeList[0].setheading(90)
    def Down(self):
        print("Down")
        if self.SnakeList[0].heading() == 90:
            return
        else:
            self.SnakeList[0].setheading(270)
    def Right(self):
        print("right")
        if self.SnakeList[0].heading() == 180:
            return
        else:
            self.SnakeList[0].setheading(0)
    def Left(self):
        print("left")
        if self.SnakeList[0].heading() == 0:
            return
        else:
            self.SnakeList[0].setheading(180)
    def snakeForward(self,SnakeList,times=8):

        for seg in range(len(self.SnakeList)-1,0,-1):#start,stop and step
                        self.newX = self.SnakeList[seg-1].xcor()
                        self.newY = self.SnakeList[seg-1].ycor()

                        self.SnakeList[seg].goto(self.newX,self.newY)

        self.SnakeList[0].forward(20)
        self.X = self.SnakeList[0].xcor()
        self.Y = self.SnakeList[0].ycor()
        self.heading = self.SnakeList[0].heading()

