from Task3 import obj_v_parser
from Task1 import save_image
import numpy as np

def build_vertex_model(vertex_array):
    matrix = np.zeros((1000, 1000), dtype = np.uint8)
    for i in range(len(vertex_array)):
        x = round(9900 * vertex_array[i][0] + 500)
        y = round(9900 * vertex_array[i][1] + 5)
        matrix[x, y] = 255

    return np.rot90(matrix)

v_array = obj_v_parser('CG\\LAB1\\data\\model_1.obj')
matrix1 = build_vertex_model(v_array)
save_image(matrix1, "CG\\LAB1\\data\\bunny.png")

