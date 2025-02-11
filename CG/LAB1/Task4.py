from Task3 import obj_v_parser
from Task1 import save_image
from PIL import Image
import numpy as np

v_array = obj_v_parser("CG\LAB1\data\model_1.obj")

img = np.ndarray((1000, 1000), dtype=np.uint8)


save_image(img, "CG\\LAB1\\data\\figure.png")

