from numpy.matrixlib.defmatrix import matrix

from Task5 import obj_v_f_parser
from Task2 import bresenham_line
from Task1 import save_image
import numpy as np

def build_model(vf: dict) -> np.ndarray:
    matrix = np.zeros((1000, 1000), dtype = np.uint8)
    for i in range(len(vf['f'])):
        p1 = vf['f'][i][0] - 1
        p2 = vf['f'][i][1] - 1
        p3 = vf['f'][i][2] - 1

        x1 = round(9900 * vf['v'][p1][0] + 500)
        y1 = round(9900 * vf['v'][p1][1] + 5)
        x2 = round(9900 * vf['v'][p2][0] + 500)
        y2 = round(9900 * vf['v'][p2][1] + 5)
        x3 = round(9900 * vf['v'][p3][0] + 500)
        y3 = round(9900 * vf['v'][p3][1] + 5)

        bresenham_line(matrix, x1, y1, x2, y2, 255)
        bresenham_line(matrix, x2, y2, x3, y3, 255)
        bresenham_line(matrix, x3, y3, x1, y1, 255)

    return np.rot90(matrix)

if __name__ == '__main__':
    vf_dict = obj_v_f_parser('CG\\LAB1\\data\\model_1.obj')
    matrix = build_model(vf_dict)
    save_image(matrix, 'CG\\LAB1\\data\\bunny.png')