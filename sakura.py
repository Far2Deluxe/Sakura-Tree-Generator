import turtle
import random

def draw_branch(branch_length, t):
    if branch_length > 5:
        if 8 < branch_length < 12:
            t.color('pink' if random.randint(0, 2) == 0 else 'brown')
        else:
            t.color('brown')
        t.pensize(branch_length / 10)
        t.forward(branch_length)
        a = 1.5 * random.random()
        t.right(20 * a)
        draw_branch(branch_length - 12 * random.random(), t)  # Increased decrement
        t.left(40 * a)
        draw_branch(branch_length - 12 * random.random(), t)  # Increased decrement
        t.right(20 * a)
        t.up()
        t.backward(branch_length)
        t.down()

def sakura_tree():
    screen = turtle.Screen()
    screen.tracer(0, 0)  # Disable animation
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    draw_branch(60, t)
    screen.update()  # Update the screen once at the end
    turtle.done()

sakura_tree()
