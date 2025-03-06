from random import randint

import numpy as np
from PIL import Image


def bary(x0, y0, x1, y1, x2, y2, x, y):
    lambda0 = ((x - x2) * (y1 - y2) - (x1 - x2) * (y - y2)) / ((x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2))
    lambda1 = ((x0 - x2) * (y - y2) - (x - x2) * (y0 - y2)) / ((x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2))
    lambda2 = 1.0 - lambda0 - lambda1

    return [lambda0, lambda1, lambda2]

def draw_tr(x0, y0, x1, y1, x2, y2, img_matrix):
    x_min, x_max = int(min(x0, x1, x2)), int(max(x0, x1, x2) + 1)
    if x_min < 0: x_min = 0
    if x_max > img_matrix.shape[0]: x_max = img_matrix.shape[1]

    y_min, y_max = int(min(y0, y1, y2)), int(max(y0, y1, y2) + 1)
    if y_min < 0: y_min = 0
    if y_max > img_matrix.shape[1]: y_max = img_matrix.shape[0]

    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            l0, l1, l2 = bary(x0, y0, x1, y1, x2, y2, i, j)
            if l0 >= 0 and l1 >= 0 and l2 >= 0:
                img_matrix[j, i] = color


if __name__ == '__main__':
    img = np.zeros((1000, 1000), dtype=np.uint8)
    draw_tr(1.0, 50.0, 30.0, 15.0, 150.0, 150.0, img)
    img_pil = Image.fromarray(img)
    img_pil.save("test1.png")