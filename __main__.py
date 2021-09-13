import glob #подключение модуля glob-расширение шаблонна имени пути. Находитвсе пути, соответствующие заданному шаблону.
from PIL import Image #импорт изображений из файла PIL.
import os #подключение модуля os
import argparse # подключение модуля argparse, который анализирует аргументы командной строки.
from common_utils import * # из файла импортировать*
from prop_resize import * # из файл prop_resizeа импортировать*
from crop import * # из файла crop импортировать*
from j2p import * # из файла j2p  импортировать*
from p2j import * # из файла p2j  импортировать*


def all_aug(im , res_p , res_w ,res_h ,crp_px,crp_p): # создание функции all_aug и передам в нее переменные im , res_p , res_w ,res_h ,crp_px,crp_p
    if bool(int(crp_px)) or bool(int(crp_p)): #если значение логических переменной crp_px_per илиcrp_p "правда", пресваеваем переменной im значение функции crp_px_per
        im = crp_px_per(im ,crp_px ,crp_p )
    if bool(res_w) or bool(res_h) or bool(res_p):#если значение логических переменной res_w или res_p "правда", пресваеваем переменной im значение функции wh_prop_resize_img
        im = wh_prop_resize_img(im,res_p , res_w ,res_h)  
    return im # присваеваем функции all_aug  значение переменной im

def main_func(args): # создание функции all_aug и передам в нее переменную args 
    scr_folder = args.scr_folder ; dest_folder = args.dest_folder
    res_p = args.res_p ; res_w = args.res_w ;res_h = args.res_h  ,crp_px = args.crp_px ,crp_p= args.crp_pargs 
    p2j_conv = args.p2j ; j2p_cov = args.j2p

    img_files = []
    for ext in ['jpg','JPG','JPEG','jpeg','png','PNG']: # цикл
        im_files = glob.glob(os.path.join(scr_folder,'*.'+ext))#присваевание переменной im_files значение glob.glob 
        img_files += im_files #присваевание переменной im_files значение предыдущей переменной im_files и следующей
    print(img_files) #вывод на экран img_files
    for img in img_files: #цикл
        file_name = img.split("\\")[-1]# присвоение переменной file_name значение img.split
        im = Image.open(img)#присвоение im переменной значение Image.open
        im = all_aug(im , res_p , res_w ,res_h ,crp_px,crp_p)#присвоение im переменной значение all_aug
        im = im.save(os.path.join(dest_folder,file_name))# присвоение im переменной значение im.save
    if p2j_conv:
        png2jpg(dest_folder,dest_folder)
    if j2p_cov:
        jpg2png(dest_folder,dest_folder)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scr_folder',default = 'G:\EPAi\epai_session11\modified_images', help='source folder ')
    parser.add_argument('--dest_folder',default = 'new' , help='destination folder ')
    parser.add_argument('--crop_px',default = 0 , help='No of pixel ')
    parser.add_argument('--crp_p',default = 0 , help='percentage of pixel')
    parser.add_argument('--res_p',default = 0 , help='percentage ')
    parser.add_argument('--res_w',default = 0 , help='res_w ')
    parser.add_argument('--res_h',default = 0 , help='res_h ')
    parser.add_argument('--j2p',default = False , help='j2p ')
    parser.add_argument('--p2j',default = False , help='p2j ')
    args = parser.parse_args()
    main_func(args)
