import numpy as np
from PIL import Image

def save_image(img: np.ndarray, filename: str) -> None:
    """Генерация и сохранение изображения"""
    img_pil = Image.fromarray(img) # Генерация изображения из массива
    img_pil.save(filename) # Сохранение изображения с указанным именем

# Task 1.1
def create_black_image(H: int, W: int) -> None:
    img = np.zeros((H, W), dtype=np.uint8) # Нулевая матрица размера H*W

    save_image(img, "bi.png")

# Task 1.2
def create_white_image(H: int, W: int) -> None:
    img = np.full((H, W), 255, dtype=np.uint8) # Матрица со значениями 255 размера H*W

    save_image(img, "wi.png")

# Task 1.3
def create_red_image(H: int, W: int) -> None:
    img = np.full((H, W, 3), (255, 0 , 0), dtype=np.uint8) # Матрица со значениями (255, 0, 0) размера H*W*3

    save_image(img, "ri.png")

#Task 1.4
def create_grad_image(H: int, W: int) -> None:
    img = np.zeros((H, W, 3), dtype=np.uint8)

    # Заполнение матрицы
    for y in range (H):
        for x in range (W):
            val = (x + y) % 256 # Расчет цвета
            img[y, x] = (val, val, val)
    
    save_image(img, "gi.png")

create_black_image(100, 100) # Создание черного изображения
create_white_image(100, 100) # Создание белого изображения
create_red_image(100, 100) # Создание красного изображения
create_grad_image(100, 100) # Создание градиентного изображения