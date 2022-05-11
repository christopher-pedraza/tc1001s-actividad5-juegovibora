"""
Actividad 5: Juego de la Víbora

Equipo 9:
Christopher Gabriel Pedraza Pohlenz A01177767
Kevin Susej Garza Aragón A00833985
Eugenia Ruiz Velasco Olvera A01177887
"""


# Se importan las librerías de random, turtle y freegames
from random import *
from turtle import *
from freegames import square, vector

# Vectores de posición y dirección iniciales
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Colores aleatorios para serpiente y comida
colores_s = ["blue", "green", "purple", "orange", "magenta"]
color_serp = colores_s[randint(0,4)]
colores_c = ["#808A87", "#CDC8B1", "#8B6508", "#8B4500", "#2F4F4F"]
color_comida = colores_c[randint(0,4)]

# Función para cambiar la dirección de la serpiente
# Recibe: componentes de dirección
def change(x, y):
    aim.x = x
    aim.y = y


# Función para comprobar que la cabeza de la serpiente este dentro de la ventana
# Recibe: vector de posición de la cabeza
# Regresa: True - dentro de límites, False - fuera
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190


# Función para mover la serpiente y la comida
def move():
    # Mueve la cabeza una posición en la dirección del vector
    head = snake[-1].copy()
    head.move(aim)

    # Si la cabeza sale de los límites, pierde 
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    # Agrega en la última posición de la serpiente
    snake.append(head)

    # Mueve la comida aleatoriamente
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
    
    # Si la posición de la cabeza es igual a la de la comida
    if head == food:
        # Imprimir longitud de la serpiente
        print('Snake:', len(snake))
        # Mover comida de posición
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # Elimina la primera posición de la lista
        snake.pop(0)
    
    # Elimina los dibujos en la pantalla
    clear()

    # Volver a dibujar serpiente y comida
    for body in snake:
        square(body.x, body.y, 9, color_serp)

    square(food.x, food.y, 9, color_comida)
    update()
    # Corre esta función despues de cien milisegundos
    ontimer(move, 100)


# Establecer el ancho, largo, y posición inicial en x y y
setup(420, 420, 370, 0)
# Esconder el cursor, la tortuga
hideturtle()
# Elimina la animación de la tortuga
tracer(False)
# Empieza a "escuchar" las teclas que se presionan
listen()
# onkey(func, key) une una función a una tecla, para que se llame a esta cuando se presiona la tecla
# Cambia el vector de dirección de la serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
# Llama a la función move
move()
# Comienza el ciclo de eventos
done()
