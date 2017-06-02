import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    dark = turtle.Turtle()
    dark.shape("turtle")
    dark.color("orange")
    dark.speed(2)
    dark.forward(100)
    dark.right(90)
    dark.forward(100)
    dark.right(90)
    dark.forward(100)
    dark.right(90)
    dark.forward(100)
    dark.right(90)


    window.exitonclick()

draw_square()
