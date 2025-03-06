from numpy import ndarray, zeros, full, uint8
from PIL import Image

def save_image(img: ndarray, filename: str) -> None:
    img_pil = Image.fromarray(img) # Генерация изображения из массива
    img_pil.save(filename) # Сохранение изображения с указанным именем

# Task 1.1
def create_black_image(H: int, W: int) -> None:
    """
    Создает и сохраняет черное 8-битное grayscale изображение заданных размеров.

    Результат сохраняется в файл "example.png" в текущей директории. Если файл с таким
    именем уже существует, он будет перезаписан.

    Args:
        H (int): Высота изображения в пикселях (положительное целое число).
        W (int): Ширина изображения в пикселях (положительное целое число).

    Example:
        >>> create_black_image(100, 200)  # Создает изображение 200x100 пикселей
    """

    img = zeros((H, W), dtype=uint8) # Нулевая матрица размера H*W

    save_image(img, "squares/bi.png")

# Task 1.2
def create_white_image(H: int, W: int) -> None:
    """
    Создает и сохраняет белое 8-битное grayscale изображение заданных размеров.

    Результат сохраняется в файл "example.png" в текущей директории. Если файл с таким
    именем уже существует, он будет перезаписан.

    Args:
        H (int): Высота изображения в пикселях (положительное целое число).
        W (int): Ширина изображения в пикселях (положительное целое число).

    Example:
        >>> create_black_image(100, 200)  # Создает изображение 200x100 пикселей
    """

    img = full((H, W), 255, dtype=uint8) # Матрица со значениями 255 размера H*W

    save_image(img, "squares/wi.png")

# Task 1.3
def create_red_image(H: int, W: int) -> None:
    """
    Создает и сохраняет изображение в формате RGB, где все пиксели имеют цвет (255, 0, 0) (красный)

    Результат сохраняется в файл "example.png" в текущей директории. Если файл с таким
    именем уже существует, он будет перезаписан.

    Args:
        H (int): Высота генерируемого изображения в пикселях. Должна быть положительным целым числом.
        W (int): Ширина генерируемого изображения в пикселях. Должна быть положительным целым числом.

    Example:
        >>> create_red_image(300, 400) # Создает красное изображение размером 300x400 пикселей и сохраняет его
    """

    img = full((H, W, 3), (255, 0 , 0), dtype=uint8) # Матрица со значениями (255, 0, 0) размера H*W*3

    save_image(img, "squares/ri.png")

#Task 1.4
def create_grad_image(H: int, W: int) -> None:
    """
    Создает и сохраняет градиентное изображение в формате RGB, где цвет пикселя 
    определяется как (x + y) % 256 (x, y - координаты пикселя)

    Результат сохраняется в файл "example.png" в текущей директории. Если файл с таким
    именем уже существует, он будет перезаписан.

    Args:
        H (int): Высота генерируемого изображения в пикселях. Должна быть положительным целым числом.
        W (int): Ширина генерируемого изображения в пикселях. Должна быть положительным целым числом.

    Example:
        >>> create_grad_image(300, 400) # Создает красное изображение размером 300x400 пикселей и сохраняет его
    """

    img = zeros((H, W, 3), dtype=uint8)

    # Заполнение матрицы
    for y in range (H):
        for x in range (W):
            val = (x + y) % 256 # Расчет цвета
            img[y, x] = (val, val, val)
    
    save_image(img, "squares/gi.png")

if __name__ == '__main__':
    create_black_image(100, 100)
    create_white_image(100, 100)
    create_red_image(100, 100)
    create_grad_image(100, 100)