# -*- coding: utf-8 -*-
# ahahhahaaaa
import random
import simple_draw
import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(100, 100)
# radius = 50
# for _ in  range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def buble(point, step):
    radius = 50
    for _ in range(5):
        radius += step
        color = sd.random_color()
        sd.circle(center_position=point, radius=radius,color=color)
#
# point = sd.get_point(300,300)
# buble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд
# for x in range(100, 1001, 100):
#     point = sd.get_point(x, 300)
#     buble(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков
# for y in range(100, 601, 200):
#     for x in range(100, 1001, 100):
#          point = sd.get_point(x, y)
#          buble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    buble(point=point, step=step)

sd.pause()


