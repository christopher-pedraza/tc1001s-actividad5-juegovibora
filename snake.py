"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import *
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colores_s = ["blue", "green", "purple", "orange", "magenta"]
color_serp = colores_s[randint(0,4)]
colores_c = ["#808A87", "#CDC8B1", "#8B6508", "#8B4500", "#2F4F4F"]
color_comida = colores_c[randint(0,4)]

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if randint(0, 100) < 10:
        if randint(0, 10) < 5:
            if (food.x + 10) < 180 and (food.x + 10) > -190:
                food.x += 10
        else:
            if (food.x - 10) < 180 and (food.x - 10) > -190:
                food.x -= 10
    if randint(0, 100) < 10:
        if randint(0, 10) < 5:
            if (food.y - 10) < 170 and (food.y - 10) > -190:
                food.y += 10
        else:
            if (food.y - 10) < 170 and (food.y - 10) > -190:
                food.y -= 10

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color_serp)

    square(food.x, food.y, 9, color_comida)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
