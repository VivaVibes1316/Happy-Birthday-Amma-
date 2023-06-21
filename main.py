import turtle as tur
import random

tur.hideturtle()

turt = tur.Turtle()
tur.title("HAPPY BIRTHDAY MOM!!!")
turt.width(8)
turt.color("cyan")
new = turt.getscreen()
turt.speed(10)
turt.shape("turtle")
new.bgcolor("purple")

confetti = tur.Turtle()
confetti.shape("square")
confetti.speed(0)
confetti.penup()
confetti.hideturtle()
confetti.shapesize(0.3)

turt.left(180)
turt.penup()
turt.forward(300)
turt.right(90)
turt.forward(100)
turt.pendown()

# Display H
turt.forward(50)
turt.right(90)
turt.forward(50)
turt.left(90)
turt.forward(50)
turt.left(90)

turt.penup()
turt.forward(50)
turt.left(90)
turt.pendown()
turt.forward(50)
turt.left(90)
turt.forward(50)
turt.right(90)
turt.forward(50)

# Display A

turt.penup()
turt.left(90)
turt.forward(15)
turt.pendown()
turt.left(70)
turt.forward(110)
turt.right(70)
turt.right(70)
turt.forward(110)
turt.left(180)
turt.forward(55)
turt.left(70)
turt.forward(38)
turt.left(70)
turt.penup()
turt.forward(55)
turt.left(110)

turt.forward(100)

# Display P

turt.left(90)
turt.pendown()
turt.forward(100)
turt.right(90)
turt.forward(50)
turt.right(20)
turt.forward(20)
turt.right(70)
turt.forward(40)
turt.right(70)
turt.forward(20)
turt.right(20)
turt.forward(50)
turt.left(90)
turt.forward(50)
turt.left(90)
turt.penup()
turt.forward(100)


# Display P

turt.left(90)
turt.pendown()
turt.forward(100)
turt.right(90)
turt.forward(50)
turt.right(20)
turt.forward(20)
turt.right(70)
turt.forward(40)
turt.right(70)
turt.forward(20)
turt.right(20)
turt.forward(50)
turt.left(90)
turt.forward(50)
turt.left(90)
turt.penup()
turt.forward(100)

# Display Y

turt.forward(20)
turt.pendown()
turt.left(90)
turt.forward(50)
turt.left(30)
turt.forward(60)
turt.backward(60)
turt.right(60)
turt.forward(60)
turt.backward(60)
turt.left(30)

# go to Home

turt.penup()
turt.home()

turt.color("white")
new.bgcolor("pink")
# setting second row

turt.backward(300)
turt.right(90)
turt.forward(60)
turt.left(180)


# Display B


turt.pendown()
turt.forward(100)
turt.right(90)
turt.forward(50)
turt.right(20)
turt.forward(20)
turt.right(70)
turt.forward(40)
turt.right(70)
turt.forward(20)
turt.right(20)
turt.forward(50)
turt.backward(50)
turt.left(180)
turt.right(20)
turt.forward(20)
turt.right(70)
turt.forward(40)
turt.right(70)
turt.forward(20)
turt.right(20)
turt.forward(50)
turt.right(90)
turt.forward(10)


# go to Home

turt.penup()
turt.home()

# setting up

turt.backward(200)
turt.right(90)
turt.forward(10)
turt.left(90)
turt.pendown()
turt.forward(20)
turt.penup()
turt.home()

# D

turt.backward(150)
turt.right(90)
turt.forward(60)
turt.pendown()
turt.backward(100)
turt.right(90)
turt.forward(10)
turt.backward(60)
turt.left(180)
turt.right(20)
turt.forward(20)
turt.right(70)
turt.forward(88)
turt.right(70)
turt.forward(20)
turt.right(20)
turt.forward(60)

turt.penup()
turt.home()

# set up for A

turt.backward(50)
turt.right(90)
turt.forward(65)
turt.left(90)

# printing A

turt.pendown()
turt.left(70)
turt.forward(110)
turt.right(70)
turt.right(70)
turt.forward(110)
turt.left(180)
turt.forward(55)
turt.left(70)
turt.forward(38)
turt.left(70)
turt.penup()
turt.forward(55)
turt.left(110)

turt.forward(100)

# printing Y

turt.pendown()
turt.left(90)
turt.forward(50)
turt.left(30)
turt.forward(60)
turt.backward(60)
turt.right(60)
turt.forward(60)
turt.backward(60)
turt.left(30)
turt.penup()

# 3rd row
turt.goto(-300, -200)
turt.color("blue")
new.bgcolor("gray")

# Print M
turt.pendown()
turt.forward(100)
turt.right(150)
turt.forward(80)
turt.right(60)
turt.backward(80)
turt.left(30)
turt.forward(100)
turt.penup()

# Print 0
turt.left(90)
turt.forward(50)
turt.right(90)
turt.pendown()
turt.backward(100)
turt.left(90)
turt.forward(50)
turt.right(90)
turt.forward(100)
turt.right(90)
turt.forward(50)
turt.penup()

# Print M

turt.right(180)
turt.forward(100)
turt.left(90)
turt.pendown()
turt.forward(100)
turt.right(150)
turt.forward(80)
turt.right(60)
turt.backward(80)
turt.left(30)
turt.forward(100)
turt.penup()

# setting position

turt.right(90)
turt.forward(215)
turt.right(90)
turt.forward(200)
turt.right(90)

# color

turt.color("yellow")
new.bgcolor("purple")

# set up
turt.penup()
turt.left(90)
turt.forward(80)
turt.left(90)
turt.forward(7)


turt.forward(100)

# design


# design pattern
turt.home()
turt.forward(200)
turt.pendown()

radius = 40
turt.width(2)
num_loops = 20
angle = 360 / num_loops
turt.speed(20)

for _ in range(num_loops):
    turt.circle(radius)
    turt.right(angle)

tur.penup()

colors = ["purple", "blue", "green", "yellow", "orange", "red", "cyan", "white"]

for _ in range(200):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    color = random.choice(colors)

    confetti.goto(x, y)
    confetti.color(color)
    confetti.stamp()

confetti.hideturtle()

tur.done()
