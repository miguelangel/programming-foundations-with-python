import turtle

def draw_square(some_turtle, shape, color, side_length, speed):
    some_turtle.shape(shape)
    some_turtle.color(color)
    some_turtle.speed(speed)
    for i in range(1,5):
        some_turtle.forward(side_length)
        some_turtle.right(90)

def draw_circle(some_turtle, shape, color, radius):
    some_turtle.shape(shape)
    some_turtle.color(color)
    some_turtle.circle(radius)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    for i in range(1,37):        
        draw_square(brad, "turtle", "yellow", 100, 5)
        brad.right(10)

    #Create the turtle Angie - Draws a circle
    angie = turtle.Turtle()
    draw_circle(angie, "arrow", "blue", 100)

    window.exitonclick()

draw_art()


