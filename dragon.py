import turtle

def dragon_curve(turtle, order, length, direction):
    if order == 0:
        turtle.forward(length)
    else:
        dragon_curve(turtle, order - 1, length, 1)
        turtle.right(90 * direction)
        dragon_curve(turtle, order - 1, length, -1)

turtle.speed(0)
dragon_curve(turtle, 12, 5, 1)
turtle.done()

"""or this works well also

import turtle

def dragon_curve(depth: int):

    start = "f-h"
    for i in range(depth):
        string = ""
        for j in range(len(start)):
            
            if start[j] == 'f':
                string += "f-h"
            elif start[j] == 'h':
                string += "f+h"
            else:
                string += start[j]
            
        start = string
        
    return start


def main():

    t.left(90)
    string = dragon_curve(depth=10)

    rules = {
            'f': [t.forward, 10],
            'h': [t.forward, 10],
            '+': [t.right, 90],
            '-': [t.left, 90],
        }
    
    for i in range(len(string)):
        rules.get(string[i])[0](rules.get(string[i])[1])        


t = turtle.Turtle()
main()
turtle.mainloop()
turtle.done()"""

# import turtle

# def dragon_curve(order, length, angle, turn):
#     if order == 0:
#         turtle.forward(length)
#         return
#     else:
#         dragon_curve(order - 1, length, angle, "right")
#         turtle.left(angle if turn == "right" else -angle)
#         dragon_curve(order - 1, length, angle, "left")

# # Configure turtle
# screen = turtle.Screen()
# screen.title("Dragon Curve")
# screen.bgcolor("white")

# t = turtle.Turtle()
# t.speed(0)
# t.penup()
# t.goto(-200, 0)
# t.pendown()

# # Parameters
# order = 4  # Adjust the order as needed
# length = 5
# angle = 90

# # Generate Dragon Curve
# dragon_curve(order, length, angle, "right")

# # Hide turtle
# t.hideturtle()

# # Keep window open until it's closed by the user
# turtle.done()