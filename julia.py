# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 22:25:58 2024

@author: S HITESH
"""

import turtle
import math

# Define global variable max_iter
max_iter = 20

# Julia set function
def julia(z, c, max_iter=max_iter):
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z ** 2 + c
    return max_iter

# Screen size (in pixels)
screenx, screeny = 200, 200

# Complex plane limits
complexPlaneX, complexPlaneY = (-2.0, 2.0), (-1.0, 2.0)

# Discretization step
step = 1

# Turtle config
turtle.tracer(0, 0)
turtle.setup(screenx, screeny)

screen = turtle.Screen()
screen.bgcolor("black")
screen.title(f"Julia Set (c = complex(-0.4, 0.6))")

# Choose a complex constant c for the Julia set
c = complex(-0.4, 0.6)

# Create a turtle for drawing
jTurtle = turtle.Turtle()
jTurtle.penup()
jTurtle.shape("square")

# px * pixelToX = x in complex plane coordinates
pixelToX, pixelToY = (complexPlaneX[1] - complexPlaneX[0])/screenx, (complexPlaneY[1] - complexPlaneY[0])/screeny

# Plot
for px in range(-int(screenx/2), int(screenx/2), step):
    for py in range(-int(screeny/2), int(screeny/2), step):
        # Calculate complex plane coordinates
        x, y = px * pixelToX, py * pixelToY
        
        # Calculate the number of iterations until divergence
        m = julia(complex(x, y), c)
        
        # Choose a color based on the number of iterations
        color_intensity = m / max_iter
        color = (color_intensity, 0.5, 1 - color_intensity)
        
        # Set color and draw dot
        jTurtle.color(color)
        jTurtle.dot(2, color)
        jTurtle.goto(px, py)
        
    turtle.update()

turtle.mainloop()