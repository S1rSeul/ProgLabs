from numpy import ndarray, arange, zeros, uint8
from math import sqrt, cos, sin, pi
from typing import Callable
from Task1 import save_image

# Интерполяция x и y между начальным и конечным значением
def dotted_line(image: ndarray, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
    step = 1.0 / 200
    for t in arange(0, 1, step):
        x = round((1.0 - t) * x0 + t * x1)
        y = round((1.0 - t) * y0 + t * y1)
        image[y, x] = color

# Фикс dotted_line с вычислением расстояния между конечной и начальной точкой
def dotted_line_v2(image: ndarray, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
    step = 1.0 / sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    for t in arange(0, 1, step):
        x = round((1.0 - t) * x0 + t * x1)
        y = round((1.0 - t) * y0 + t * y1)
        image[y, x] = color

# Использование цикла по x, а не по t
def x_loop_line(image: ndarray, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
    for x in range(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round((1.0 - t) * y0 + t * y1)
        image[y, x] = color

# Фикс#1 x_loop_line - теперь точки меньшие x0 отрисовываются правильно
def x_loop_line_fix1(image: ndarray, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    for x in range(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round((1.0 - t) * y0 + t * y1)
        image[y, x] = color

# Фикс#2 x_loop_line - теперь точки с большим тангенсом отрисовываются правильно
def x_loop_line_fix2(image: ndarray, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
    xchange = False
    if abs(x0 - x1) < abs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if xchange:
        for x in range(x0, x1):
            t = (x - x0) / (x1 - x0)
            y = round((1.0 - t) * y0 + t * y1)
            image[x, y] = color
    else:
        for x in range(x0, x1):
            t = (x - x0) / (x1 - x0)
            y = round((1.0 - t) * y0 + t * y1)
            image[y, x] = color

# Сочетание Фиксов #1 и #2 x_loop_line - полноценно работающая функция
def x_loop_line_v2(image: ndarray, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
    xchange = False
    if abs(x0 - x1) < abs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    if xchange:
        for x in range(x0, x1):
            t = (x - x0) / (x1 - x0)
            y = round((1.0 - t) * y0 + t * y1)
            image[x, y] = color
    else:
        for x in range(x0, x1):
            t = (x - x0) / (x1 - x0)
            y = round((1.0 - t) * y0 + t * y1)
            image[y, x] = color

# Без непосредственных вычислений координаты y
def x_loop_line_v2_no_y_calc(image: ndarray, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
    xchange = False
    if abs(x0 - x1) < abs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    y = y0
    dy = abs(y1 - y0) / (x1 - x0)
    derr = 0.0
    y_update = 1 if y1 > y0 else -1

    if xchange:
        for x in range(x0, x1):
            image[x, y] = color
            derr += dy
            if derr > 0.5:
                derr -= 1.0
                y += y_update
    else:
        for x in range(x0, x1):
            image[y, x] = color
            derr += dy
            if derr > 0.5:
                derr -= 1.0
                y += y_update

# Домножение всех вычислений шага на 2*(x1-x0) с целью приведения вычислений к int
def x_loop_line_v2_no_y_calc_v2(image: ndarray, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
    xchange = False
    if abs(x0 - x1) < abs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    y = y0
    dy = 2 * (x1 - x0) * abs(y1 - y0) / (x1 - x0)
    derr = 0
    y_update = 1 if y1 > y0 else -1

    if xchange:
        for x in range(x0, x1):
            image[x, y] = color
            derr += dy
            if derr > 2 * (x1 - x0) * 0.5:
                derr -= 2 * (x1 - x0) * 1.0
                y += y_update
    else:
        for x in range(x0, x1):
            image[y, x] = color
            derr += dy
            if derr > 2 * (x1 - x0) * 0.5:
                derr -= 2 * (x1 - x0) * 1.0
                y += y_update

# Окончательный результат - алгоритм Брезенхема
def bresenham_line(image: ndarray, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
    xchange = False
    if abs(x0 - x1) < abs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    y = y0
    dy = 2 * abs(y1 - y0)
    derr = 0
    y_update = 1 if y1 > y0 else -1

    if xchange:
        for x in range(x0, x1):
            image[y, x] = color
            derr += dy
            if derr > (x1 - x0):
                derr -= 2 * (x1 - x0)
                y += y_update
    else:
        for x in range(x0, x1):
            image[x, y] = color
            derr += dy
            if derr > (x1 - x0):
                derr -= 2 * (x1 - x0)
                y += y_update

def create_star(draw_function: Callable[[ndarray, int, int, int, int, int], None]):
    matrix = zeros((200, 200), dtype=uint8)
    for i in range(13):
        alpha = 2 * pi * i / 13
        x_end = round(100 + 95 * cos(alpha))
        y_end = round(100 + 95 * sin(alpha))
        
        draw_function(matrix, 100, 100, x_end, y_end, 255)
    
    save_image(matrix, "stars/star.png")

if __name__ == "__main__":
    create_star(x_loop_line_v2_no_y_calc)