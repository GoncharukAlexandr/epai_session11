import PIL
import glob
import os
from common_utils import *
import argparse


def png2jpg(scr_folder,dest_folder):
    create_dir(dest_folder)
    ext_list = ['png','PNG']
    to_be_ext = 'jpg'
    change_extension(to_be_ext,ext_list,scr_folder,dest_folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('--convert2ext',default = 'png', help='convert to ')
    # parser.add_argument('--convert_ext_list',default = ['jpg','JPG','JPEG','jpeg'], help='extentions to be converted ')
    parser.add_argument('--scr_folder',default = 'G:\EPAi\epai_session11\modified_images', help='convert to ')
    parser.add_argument('--dest_folder',default = 'G:\EPAi\epai_session11\new' , help='extentions to be converted ')
    args = parser.parse_args()
    png2jpg(scr_folder = args.scr_folder,dest_folder = args.dest_folder)