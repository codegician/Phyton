import turtle

def factorial(use_turtle):
    for i in range (1,4):
        use_turtle.forward(100)
        use_turtle.left(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    dark = turtle.Turtle()
    dark.shape("classic")
    dark.color("white")
    dark.speed(8)

    for i in range(1, 36):
        factorial(dark)
        dark.right(10)

    for i in range(1,36):
        dark.circle(50)
        dark.right(10)

    
    window.exitnclick()

draw_art()
