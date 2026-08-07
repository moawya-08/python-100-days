def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_on_right():
        turn_left()
    if right_is_clear and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    elif front_is_clear():
        move()
