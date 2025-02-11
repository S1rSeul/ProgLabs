from numpy.matrixlib.defmatrix import matrix

from Task5 import obj_v_f_parser
from Task2 import bresenham_line
from Task1 import save_image
import numpy as np

def build_model(v_array: list, f_array: list):
    matrix = np.zeros((1000, 1000), dtype = np.uint8)
    for i in range(len(f_array)):
        p1 = f_array[i][0] - 1
        p2 = f_array[i][1] - 1
        p3 = f_array[i][2] - 1

        x1 = round(9900 * v_array[p1][0] + 500)
        y1 = round(9900 * v_array[p1][1] + 5)
        x2 = round(9900 * v_array[p2][0] + 500)
        y2 = round(9900 * v_array[p2][1] + 5)
        x3 = round(9900 * v_array[p3][0] + 500)
        y3 = round(9900 * v_array[p3][1] + 5)

        bresenham_line(matrix, x1, y1, x2, y2, 255)
        bresenham_line(matrix, x2, y2, x3, y3, 255)
        bresenham_line(matrix, x3, y3, x1, y1, 255)

    return np.rot90(matrix)

if __name__ == '__main__':
    v_array = []
    f_array = []
    obj_v_f_parser('data/model_1.obj', v_array, f_array)
    matrix = build_model(v_array, f_array)
    save_image(matrix, 'data/super_bunny.png')