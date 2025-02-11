from Task3 import obj_v_parser
from Task1 import save_image
from PIL import Image
import numpy as np

def build_vertex_model(vertex_array):
    matrix = np.zeros((1000, 1000), dtype = np.uint8)
    for i in range(len(vertex_array)):
        x = round(vertex_array[i][0])
        y = round(vertex_array[i][1])
        matrix[y, x] = 255

    return matrix

v_array = obj_v_parser('CG\\LAB1\\data\\model_1.obj')
matrix1 = build_vertex_model(v_array)
save_image(matrix1, "CG\\LAB1\\data\\figure.png")

