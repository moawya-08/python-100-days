import turtle
import random
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colours = (r,g,b)
    return colours
    
def draw_circle():
    tim.pencolor(random_colour())
    tim.circle(100)
    tim.speed("fastest")
    
for i in range(50):
    tim.left(8)
    draw_circle()






screen = Screen()
screen.exitonclick()