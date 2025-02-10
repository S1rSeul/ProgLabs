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

v_array = obj_v_parser('model_1.obj')
print(v_array)