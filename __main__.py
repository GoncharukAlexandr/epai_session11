import glob
from PIL import Image
import os 
import argparse
from common_utils import *
from prop_resize import *
from crop import *
from j2p import *
from p2j import *


def all_aug(im , res_p , res_w ,res_h ,crp_px,crp_p):
    if bool(int(crp_px)) or bool(int(crp_p)):
        im = crp_px_per(im ,crp_px ,crp_p )
    if bool(w_per) or bool(h_per) or bool(res_p):
        im = wh_prop_resize_img(im,res_p , res_w ,res_h)  
    return im
def main(args):
    scr_folder = args.scr_folder ; dest_folder = args.dest_folder
    res_p = agrs.res_p ; res_w = args.res_w ;res_h = args.res_h  ,crp_px = args.crp_px ,crp_p= args.crp_p
    p2j_conv = args.p2j ; j2p_cov = args.j2p

    img_files = []
    for ext in ['jpg','JPG','JPEG','jpeg','png','PNG']:
        im_files = glob.glob(os.path.join(scr_folder,'*.'+ext))
        img_files += im_files
    print(img_files)
    for img in img_files:
        im = Image.open(img)
        im = all_aug(im , res_p , res_w ,res_h ,crp_px,crp_p)
        im = im.save(os.path.join(dest_folder,file_name)) 
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

