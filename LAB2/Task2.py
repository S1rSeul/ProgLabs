import numpy as np
from LAB1.Task1 import save_image
from LAB1.Task5 import obj_vf_parser
from LAB2.Task1 import draw_tr

def build_model(vf):
    matrix = np.full((1000, 1000, 3), (0, 0, 0), dtype=np.uint8)
    for i in range(len(vf['f'])):
        p1, p2, p3 = [vi - 1 for vi in vf['f'][i]]

        x1 = (9900 * vf['v'][p1][0] + 500)
        y1 = (9900 * vf['v'][p1][1] + 5)

        x2 = (9900 * vf['v'][p2][0] + 500)
        y2 = (9900 * vf['v'][p2][1] + 5)

        x3 = (9900 * vf['v'][p3][0] + 500)
        y3 = (9900 * vf['v'][p3][1] + 5)

        draw_tr(x1, y1, x2, y2, x3, y3, matrix)

    return matrix

if __name__ == '__main__':
    vf_dict = obj_vf_parser("data/model.obj")
    matrix = build_model(vf_dict)
    save_image(matrix, 'bunny.png')