def obj_vf_parser(filename: str) -> dict:
    """Парсер строк, содержащих информацию о вершинах объекта и о ребрах объекта в файле типа OBJ"""

    lines = []  # Массив для хранения строк из файла

    try:
        # Открываем и построчно читаем файл
        with open(filename) as file:
            lines = file.readlines()

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

    vf = dict(v = [], f = [])

    for line in lines:
        if line.startswith('v '):
            # Разбиваем строку по пробелам на подстроки
            parts = line.strip().split()
            # Приводим строки к вещественным числам и заносим в массив
            v_numbers = [float(parts[1]), float(parts[2]), float(parts[3])]

            vf['v'].append(v_numbers)

        if line.startswith('f '):
            parts = line.strip().split() # Разбиваем строку по пробелам на подстроки
            f_numbers = []

            for part in parts[1:]: # Пропускаем первую часть 'f'
                f_value = part.split('/')[0] # Делим части по '/' и выделяем только 1-ю часть
                f_numbers.append(int(f_value)) # Приводим строку к целому числу и заносим в массив

            vf['f'].append(f_numbers)

    return vf