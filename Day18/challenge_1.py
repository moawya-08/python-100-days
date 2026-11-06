from random import choice
from turtle import Screen, Turtle, showturtle

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

timmy = Turtle()
def shape(sides):
    for i in range(sides):
        bend = 360/sides
        timmy.forward(100)
        timmy.right(bend)
        timmy.forward(100)

for sides_in_num in range(3,11):
    timmy.pencolor(choice(colours))
    shape(sides_in_num)
    

screen = Screen()
screen.exitonclick()