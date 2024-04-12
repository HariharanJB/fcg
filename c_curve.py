from turtle import *
color('red', 'blue')
#begin_fill()
rule=['r','f','l','l','f','r']
prev=['r','f','l','l','f','r']
ans=[]
for iter in range(6):
    ans = []
    for i in prev:
        if(i=='f'):
            ans+=rule
        else:
            ans.append(i)
    prev = ans

print(ans)

for i in range(0,len(ans)):
    if(ans[i] == 'r'):
        right(45)
    elif(ans[i] == 'f'):
        forward(20)
    elif(ans[i] == 'l'):
        left(45)


#end_fill()
done()

"""or this works well also

import turtle

def c_curve(depth: int):
    
    start = "+f--f+"
    for i in range(depth):
        string = ""
        for j in range(len(start)):
            
            if start[j] == 'f':
                string += "+f--f+"
            else:
                string += start[j]
        start = string
        
    return start

def main():
    
    string = c_curve(depth=4)
    rules = {
            'f': [t.forward, 10],
            '+': [t.right, 45],
            '-': [t.left, 45],
        }
    
    for i in range(len(string)):
        rules.get(string[i])[0](rules.get(string[i])[1])        


t = turtle.Turtle()
main()
turtle.mainloop()
turtle.done()"""

# import turtle

# # C Curve function
# def c_curve(n):
#     if n == 0:
#         return ['F']
#     else:
#         prev = c_curve(n - 1)
#         return prev + ['L'] + [x if x == 'F' else 'R' for x in reversed(prev)]

# # Configure turtle
# screen = turtle.Screen()
# screen.title("C Curve")
# screen.bgcolor("white")

# t = turtle.Turtle()
# t.speed(0)
# t.penup()
# t.goto(-200, 0)
# t.pendown()

# # Parameters
# order = 4 # Adjust the order as needed
# size = 6

# # Generate C Curve
# curve = c_curve(order)
# for move in curve:
#     if move == 'F':
#         t.forward(size)
#     elif move == 'L':
#         t.left(90)
#     elif move == 'R':
#         t.right(90)

# # Hide turtle
# t.hideturtle()

# # Keep window open until it's closed by the user
# turtle.done()