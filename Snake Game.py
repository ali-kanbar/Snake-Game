from turtle import Screen,Turtle
import time
from random import randint

screen = Screen()
positions = [(0,0),(-20,0),(-40,0)]
try:
    file = open("Snake Game Highscore.txt", "r+")
    high_score = int(file.read())
except FileNotFoundError:
    file = open("Snake Game Highscore.txt", "w")
    file.write("0")
    high_score = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "Right"
        
    def create_snake(self):
        for position in positions:
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(position)
            self.speed = 0.05
            self.segments += [t]
           
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].position())
        self.head.fd(20)

    def up(self):
        if self.direction != "Down":  
            self.head.setheading(90)
            self.direction = "Up"  

    def down(self):
        if self.direction != "Up":
            self.head.setheading(270)
            self.direction = "Down"

    def right(self):
        if self.direction != "Left":
            self.head.setheading(0)
            self.direction = "Right"

    def left(self):
        if self.direction != "Right":
            self.head.setheading(180)
            self.direction = "Left"
            
    def get_bigger(self):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments += [t]
        
    def snake_reset(self):
        for item in self.segments:item.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
class Food(Turtle):
    def __init__(self):
        super().__init__() 
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5,stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        x = randint(-280,280)
        y = randint(-280,240)
        self.goto(x,y)
        
    def change_position(self):
        x = randint(-280,280)
        y = randint(-280,240)
        self.goto(x,y)
        
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.goto(x = 0,y = 260)
        self.score = 0
        self.high_score = high_score
        self.write("Score : 0"+" High Score : "+str(self.high_score),align = "center",font = ("Courier",24,"normal"))
    
    def scoreboard_reset(self):
        if self.score > self.high_score:
            file.seek(1)
            file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write("Score : "+str(self.score)+" High Score : " +str(self.high_score),align = "center",font = ("Courier",24,"normal"))
        
    def change_score(self):
        self.clear()
        self.score += 1
        self.write("Score : "+str(self.score)+" High Score : " +str(self.high_score),align = "center",font = ("Courier",24,"normal"))
    
screen.tracer(0)
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_on = True
while game_on:
    screen.update()
    time.sleep(snake.speed)
    snake.move()
    if snake.head.distance(food) < 20:
        food.change_position()
        snake.get_bigger()
        scoreboard.change_score()
        if snake.speed > 0.02:
            snake.speed -= 0.0025
            
    if abs(snake.head.xcor()) >= 300 or abs(snake.head.ycor()) >= 300:
        scoreboard.scoreboard_reset()
        snake.snake_reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.scoreboard_reset()
            snake.snake_reset()
        
    
file.close()
screen.exitonclick()