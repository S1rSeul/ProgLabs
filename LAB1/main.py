from Task6 import build_model
from Task5 import obj_v_f_parser
from Task2 import save_image

if __name__ == '__main__':

    print("Вы хотите нарисовать зайца?")
    input()
    print("ВЫ ТОЧНО ХОТИТЕ НАРИСОВАТЬ ЗАЙЦА?")
    input()

    vf_dict = obj_v_f_parser('CG\\LAB1\\data\\model_1.obj')
    matrix = build_model(vf_dict)
    save_image(matrix, 'CG\\LAB1\\data\\bunny.png')