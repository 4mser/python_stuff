
# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math
 
def fiboPlot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b
 
    # Setting the colour of the plotting pen to gray
    x.pencolor("gray")
    x.pensize(3)
    x.speed(6)
    
 
    # Drawing the first square
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
 
    # Proceeding in the Fibonacci Series
    temp = square_b
    square_b = square_b + square_a
    square_a = temp
     
    # Drawing the rest of the squares
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
 
        # Proceeding in the Fibonacci Series
        temp = square_b
        square_b = square_b + square_a
        square_a = temp
 
    # Bringing the pen to starting point of the spiral plot
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()
 
    # Setting the colour of the plotting pen to white
    x.pencolor("white")
 
    x.speed(0)
    # Fibonacci Spiral Plot
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b
 
 
# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 2
 
# Taking Input for the number of
# Iterations our Algorithm will run
n = int(input('Enter the number of iterations (must be > 1): '))
 
# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if n > 0:
    print("Fibonacci series for", n, "elements :")
    x = turtle.Turtle()
    x.getscreen().bgcolor('black')
    x.speed(0)
    fiboPlot(n)
    x.penup()
    turtle.done()
    
else:
    print("Number of iterations must be > 0")

# import turtle

# t = turtle.Turtle()

# a, b = 0, 1

# t.penup()
# t.goto(-200, 0)
# t.pendown()
# t.setheading(90)

# while a < 1000:
#     t.forward(a)
#     t.right(90)
#     temp = a
#     a = b
#     b = temp + b

# turtle.done()
