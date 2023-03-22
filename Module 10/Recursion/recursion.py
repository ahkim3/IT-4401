# Draw a snowman and snowflake using recursion


import turtle


def snowman(size, x, y):
    if size < 60:  # Base case
        return
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(size)

    # Recursive calls
    snowman(size*0.8, x, y+size*1.2)
    snowman(size*0.6, x, y+size*2.2)


def snowflake(size):
    if size < 5:  # Base case
        return
    for i in range(6):
        turtle.forward(size)
        snowflake(size/3)  # Recursive call
        turtle.backward(size)
        turtle.right(60)  # Rotate 60 degrees


# Background and pen settings
turtle.speed(0)
turtle.ht()
turtle.bgcolor("light blue")
turtle.color("white")
turtle.pensize(2)

# Draw snowman
snowman(100, 0, -100)

# Draw snowflake
turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()
for i in range(6):
    snowflake(100)
    turtle.right(60)

turtle.done()
