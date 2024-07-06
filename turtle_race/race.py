from turtle import *
import random

# create screen
Screen().setup(width=600, height=400)
title('Ceed Media Turtle Race')
Screen().bgcolor('burlywood')

colors = ['red', 'blue', 'green', 'brown',
          'deep pink', 'purple', 'teal', 'chocolate']

y_position = [-160, -120, -80, -20, 20, 80, 120, 160]

race_turtle = []

# design the finish line
line_values = [(280, 200, 9, 'black'), (280, 180, 8, 'white'), (240, 200, 9, 'black'),
            (240, 180, 8, 'white'), (260, 180, 8, 'black'), (260, 200, 9, 'white')]


def finish_line(x_cor, spacing, period, line_color):
    for position in range(period):
        box_shape = Turtle(shape="square")
        spacing -= 40
        box_shape.speed(0)
        box_shape.penup()
        box_shape.goto(x=x_cor, y=spacing)
        box_shape.color(line_color)

for values in line_values:
    finish_line(*values)

for index in range(8):
    turtles = Turtle(shape="turtle")
    turtles.speed(0)
    turtles.penup()
    turtles.goto(x=-290, y=y_position[index])
    turtles.color(colors[index])
    race_turtle.append(turtles)


end_race = False 
check_winner = []

while not end_race:
    for turtle in race_turtle:
        movement = random.randint(0,10)
        if turtle.xcor() > 235:
            end_race = True 
            check_winner.append(turtle.pencolor())
            turtle.turtlesize(2.0,2.0,2.0)
        turtle.pendown()
        turtle.forward(movement)

    if end_race == True and len(check_winner) == 1: 
        print(f"{''.join(map(str,check_winner))} won the race")
    elif end_race == True and len(check_winner) > 1: 
        print('The race was a draw, we have not winner')

# exit screen on click
Screen().exitonclick()
