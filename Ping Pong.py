# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

from turtle import Turtle
import turtle
import os

cursor_size = 1
player_height = 1
player_width = 5

width = 800
height = 600

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("yellow")
wn.setup(float(width), float(height))
wn.tracer(0)

#Pen 4
pen4 = turtle.Turtle()
pen4.speed(0)
pen4.shape("circle")
pen4.color("black")
pen4.penup()
pen4.hideturtle()
pen4.goto(-500, 0)
name1 = str(input("Enter Player A's Name:"))
pen4.write(name1, align="center", font=("Times New Roman", 50, "bold"))

#Pen 5
pen5 = turtle.Turtle()
pen5.speed(0)
pen5.shape("circle")
pen5.color("black")
pen5.penup()
pen5.hideturtle()
pen5.goto(500, 0)
name2 = input("Enter Player B's Name:")
pen5.write(name2, align="center", font=("Times New Roman", 50, "bold"))

# Score
score_a = 0
score_b = 0
score_c = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(float(player_width), float(player_height))
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(float(player_width), float(player_height))
paddle_b.penup()
paddle_b.goto(350, 0)

# Paddle C
paddle_c = turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("square")
paddle_c.color("black")
paddle_c.shapesize(float(player_height), float(player_width))
paddle_c.penup()
paddle_c.goto(0, -290)

print("Enter the following coordinates to detemine which player serves fist (x, y): "
      "\n a) Player A: (-300, 0), \n a) Player B: (300, 0)")

xcor = input("Enter x co-ordinate  =  ")
ycor = input("Enter y co-ordinate  =  ")

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(float(xcor), float(ycor))
ball.dx = 1.5
ball.dy = 1.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Times New Roman", 30, "bold"))

#Pen 2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("circle")
pen2.color("black")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 200)

#Pen 3
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.shape("circle")
pen3.color("black")
pen3.penup()
pen3.hideturtle()
pen3.goto(0, 360)
pen3.write("Jay's Pong Game", align="center", font=("Times New Roman", 30, "bold"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    if y < height/2 - player_height/2:
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    if y > player_height/2 - height/2:
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    if y < height/2 - player_height/2:
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    if y > player_height/2 - height/2:
        paddle_b.sety(y)

def draw_border():
    border.begin_fill()
    border.fillcolor("sky blue")
    border.pensize(5)
    border.penup()
    border.setposition(-width/2, height/2)
    border.pendown()
    border.forward(width)
    border.penup()
    border.sety(-height/2)
    border.pendown()
    border.backward(width)
    border.sety(height/2)
    border.pendown()
    border.backward(-width)
    border.sety(-height/2)
    border.end_fill()
    border.begin_fill()
    border.fillcolor("sky blue")
    border.pensize(5)
    border.penup()
    border.setposition(width/2, -height/2)
    border.pendown()
    border.forward(-width)
    border.penup()
    border.sety(height/2)
    border.pendown()
    border.backward(-width)
    border.sety(-height/2)
    border.pendown()
    border.backward(width)
    border.sety(height/2)
    border.end_fill()

def filet():
    border.penup()
    border.pensize(1)
    border.setposition(0, -height/2)
    border.setheading(90)
    border.pendown()

    for _ in range(height // 50):
        border.forward(50 / 2 + 1)
        border.penup()
        border.forward(50 / 2 + 1)
        border.pendown()

border = Turtle(visible=False)
border.speed('fastest')
border.color("black")

draw_border()
filet()

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 30, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 30, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1


    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")


    if score_a == 11:
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350,0)
        pen2.write("Congratulations, Player A!!! You won the game", align="center", font=("Times New Roman", 30, "bold"))
    elif score_b == 11:
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350,0)
        pen2.write("Congratulations, Player B!!! You won the game", align="center", font=("Times New Roman", 30, "bold"))
