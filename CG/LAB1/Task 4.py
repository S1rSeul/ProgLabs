import numpy as np
from PIL import Image

# Парсер строк, содержащих информацию о вершинах объекта в файле типа OBJ
def obj_v_parser(filename):
    # Массив для хранения числовых значений
    values = []

    # Открываем и построчно читаем файл
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Разбиваем строку по пробелам на подстроки
        parts = line.strip().split()

        # Преобразуем строки в числа и записываем в массив
        if parts[0] == 'v' and len(parts) == 4:
            numbers = [float(parts[1]), float(parts[2]), float(parts[3])]
            values.append(numbers)

    return values

def build_vertex_model(vertex_array):
    matrix = np.zeros((1000, 1000), dtype = np.uint8)
    for i in range(len(vertex_array)):
        x = vertex_array[i][0]
        y = vertex_array[i][1]
        matrix[round(8000 * x + 500), round(8000 * y + 130)] = 255

    return matrix

v_array = obj_v_parser('model_1.obj')
matrix1 = build_vertex_model(v_array)
matrix1 = np.rot90(matrix1)
img = Image.fromarray(matrix1, 'L')
img.save('Test.png')
