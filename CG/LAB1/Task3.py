
def obj_v_parser(filename: str) -> list:
    """Парсер строк, содержащих информацию о вершинах объекта в файле типа OBJ"""
    
    values = [] # Массив для хранения числовых значений
    lines = [] # Массив для хранения строк из файла

    try:
        # Открываем и построчно читаем файл
        with open(filename, 'r') as file:
            lines = file.readlines()

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

    for line in lines:
        # Разбиваем строку по пробелам на подстроки
        parts = line.strip().split()

        # Преобразуем строки в числа и записываем в массив
        if parts[0] == 'v' and len(parts) == 4:
            numbers = [float(parts[1]), float(parts[2]), float(parts[3])]
            values.append(numbers)

    return values

v_array = obj_v_parser('CG\\LAB1\\data\\model_1.obj')