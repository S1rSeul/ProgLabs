from random import randint
import numpy as np
from PIL import Image

def find_normal(x0, y0, z0, x1, y1, z1, x2, y2, z2):
    n1 = [x1 - x2, y1 - y2, z1 - z2]
    n2 = [x1 - x0, y1 - y0, z1 - z0]

    return np.cross(n1, n2)

def bary(x0, y0, x1, y1, x2, y2, x, y):
    lambda0 = ((x - x2) * (y1 - y2) - (x1 - x2) * (y - y2)) / ((x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2))
    lambda1 = ((x0 - x2) * (y - y2) - (x - x2) * (y0 - y2)) / ((x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2))
    lambda2 = 1.0 - lambda0 - lambda1

    return [lambda0, lambda1, lambda2]

def draw_tr(x0, y0, z0, x1, y1, z1, x2, y2, z2, img_matrix, z_buffer):
    n = find_normal(x0, y0, z0, x1, y1, z1, x2, y2, z2)
    l = [0, 0, 1]

    norm_scalar_mult = (np.dot(n, l)) / (np.linalg.norm(n) * np.linalg.norm(l))

    x0, x1, x2 = [9900 * i + 500 for i in [x0, x1, x2]]
    y0, y1, y2 = [9900 * i + 5 for i in [y0, y1, y2]]


    x_min, x_max = int(min(x0, x1, x2)), int(max(x0, x1, x2) + 1)
    if x_min < 0: x_min = 0
    if x_max > img_matrix.shape[0]: x_max = img_matrix.shape[1]

    y_min, y_max = int(min(y0, y1, y2)), int(max(y0, y1, y2) + 1)
    if y_min < 0: y_min = 0
    if y_max > img_matrix.shape[1]: y_max = img_matrix.shape[0]

    color = (-255 * norm_scalar_mult, 0, 0)
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            l0, l1, l2 = bary(x0, y0, x1, y1, x2, y2, i, j)
            if l0 >= 0 and l1 >= 0 and l2 >= 0 and norm_scalar_mult < 0:
                z = l0 * z0 + l1 * z1 + l2 * z2
                if z < z_buffer[j, i]:
                    img_matrix[j, i] = color
                    z_buffer[j, i] = z



if __name__ == '__main__':
    img = np.zeros((1000, 1000), dtype=np.uint8)
    draw_tr(1.0, 50.0, 30.0, 15.0, 150.0, 150.0, img)
    img_pil = Image.fromarray(img)
    img_pil.save("test1.png")