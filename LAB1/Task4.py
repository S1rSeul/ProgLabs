from numpy import zeros, uint8, rot90
from Task1 import save_image
from Task3 import obj_v_parser

def build_vertex_model(vertex_array):
    matrix = zeros((1000, 1000), dtype = uint8)
    for i in range(len(vertex_array)):
        x = round(9900 * vertex_array[i][0] + 500)
        y = round(9900 * vertex_array[i][1] + 5)
        matrix[x, y] = 255

    return rot90(matrix)

v_array = obj_v_parser("model.obj")
matrix1 = build_vertex_model(v_array)
save_image(matrix1, "bunnies/vertex_bunny.png")

