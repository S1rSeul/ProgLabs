
from typing import Tuple
from PIL import Image
import numpy as np
from random import randint

def bary(x0: float, y0: float, x1: float, y1: float, x2: float, y2: float, x: int, y: int) -> Tuple[float, float, float]:
    l0 = ((x - x2) * (y1 - y2) - (x1 - x2) * (y - y2)) / ((x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2))
    l1 = ((x0 - x2) * (y - y2) - (x - x2) * (y0 - y2)) / ((x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2))
    l2 = 1.0 - l0 - l1
    return l0, l1, l2

def draw_tr(x0: float, y0: float, x1: float, y1: float, x2: float, y2: float, img_mat: np.ndarray) -> np.ndarray:
    xmin = int(min(x0, x1, x2))
    xmax = int(max(x0, x1, x2) + 1)

    ymin = int(min(y0, y1, y2))
    ymax = int(max(y0, y1, y2) + 1)

    xmin = max(xmin, 0)
    ymin = max(ymin, 0)
    xmax = min(xmax, img_mat.shape[1])
    ymax = min(ymax, img_mat.shape[0])

    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    for i in range(xmin, xmax):
        for j in range(ymin, ymax):
            l0, l1, l2 = bary(x0, y0, x1, y1, x2, y2, i, j)
            if l0 >= 0 and l1 >= 0 and l2 >= 0:
                img_mat[j, i] = color

    return img_mat

