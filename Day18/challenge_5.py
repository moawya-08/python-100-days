from turtle import Turtle, Screen, forward
import random
import turtle

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim = Turtle()
turtle.colormode(255)
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colours = (r,g,b)
    return colours

directions= [0,90,180, 270]

for i in range(100):
    tim.pensize(15)
    random_direction = random.choice(directions)
    tim.right(random_direction)
    tim.forward(25)
    tim.pencolor(random_colour())
    tim.speed("fastest")
        
screen = Screen()
screen.exitonclick()