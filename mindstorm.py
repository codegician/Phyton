import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    dark = turtle.Turtle()
    dark.shape("turtle")
    dark.color("orange")
    dark.speed(2)
    draw_square(dark)
    
    xen = turtle.Turtle()
    xen.color("blue")
    xen.shape("arrow")
    xen.circle(100)
    
    window.exitonclick()

draw_art()
