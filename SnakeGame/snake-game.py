import turtle 
import time 
import random


delay = 0.1
gameWindow = turtle.Screen()
gameWindow.title("Snake Game")
gameWindow.bgcolor("green")
gameWindow.setup(width=600, height=600)
gameWindow.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0, 100)

scoreText = turtle.Turtle()
scoreText.speed(0)
scoreText.shape("square")
scoreText.color("red")
scoreText.hideturtle()
scoreText.penup()
scoreText.goto(0, 260)
scoreText.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))
score = 0
high_score = 0
segments = []


def get_food():
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-290, 290)        
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)
        global score, high_score 
        score +=1
        if score > high_score:
            high_score = score
        scoreText.clear()
        scoreText.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        



def move_body():
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


def move_up():
    if head.direction != "down":      
        head.direction = "up"
    
def move_down():
    if head.direction != "up":
        head.direction = "down"
    
def move_left():
    if head.direction != "right":
        head.direction = "left"
    
def move_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20) 
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20) 
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
def headColission():
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            global score
            score = 0
            scoreText.clear()
            scoreText.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            


def out_of_screen():
    x = head.position()[0]
    y = head.position()[1]
    if x > 290:
        head.goto(-290, 0)
    elif x < -290:
        head.goto(290, y)
    elif y > 290:
        head.goto(x, -290)
    elif y < -290:
        head.goto(x, 290)    
    
gameWindow.listen()
gameWindow.onkeypress(move_up, "w")
gameWindow.onkeypress(move_down, "s")
gameWindow.onkeypress(move_left, "a")
gameWindow.onkeypress(move_right, "d")


while True:
    gameWindow.update()
    #When snake gets out of screen
    out_of_screen()
    #Adding a new body  part
    get_food()
    #Moving the body parts    
    move_body()

    move()
    #Head collision with the body
    headColission()
    time.sleep(delay)
      
gameWindow.mainloop()