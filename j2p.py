import PIL
import glob
import os
from common_utils import *
import argparse


def jpg2png(scr_folder,dest_folder):
    create_dir(dest_folder)
    ext_list = ['jpg','JPG','JPEG','jpeg']
    to_be_ext = 'png'
    change_extension(to_be_ext,ext_list,scr_folder,dest_folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('--convert2ext',default = 'png', help='convert to ')
    # parser.add_argument('--convert_ext_list',default = ['jpg','JPG','JPEG','jpeg'], help='extentions to be converted ')
    parser.add_argument('--scr_folder',default = './images', help='convert to ')
    parser.add_argument('--dest_folder',default = './modified_images', help='extentions to be converted ')
    args = parser.parse_args()
    jpg2png(scr_folder = args.scr_folder,dest_folder = args.dest_folder)