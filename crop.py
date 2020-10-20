import glob
from PIL import Image
import os 
import argparse
from common_utils import *


def crp_px(im,px):
    width, height = im.size
    right = (width//2)+px
    left = (width//2)-px
    top = (height//2)-px
    bottom = (height//2)+px
    print(left, top, right, bottom)
    if right < width and bottom < height and left >0 and top > 0 :
        im1 = crop_image(im,left, top, right, bottom)
        return(im1)
    else:
        print("out of bounds")
        return(None)
    
def crp_per(im,per):
    width, height = im.size
    right = (width//2)+(width*(per//100))
    left = (width//2)-(width*(per//100))
    top = (height//2)-(height*(per//100))
    bottom = (height//2)+(height*(per//100))
    print(left, top, right, bottom)
    im1 = crop_image(im,left, top, right, bottom)
    return im1

def crp_px_per(im ,px = None,per = None ):
    if bool(int(px)):
        im = crp_px(im,int(px))
    if bool(int(per)):
        im = crp_per(im,int(per))
    return im


def crop(scr_folder,dest_folder ,px = None,per = None):
    img_files = []
    for ext in ['jpg','JPG','JPEG','jpeg','png','PNG']:
        im_files = glob.glob(os.path.join(scr_folder,'*.'+ext))
        img_files += im_files

    for img in img_files:
        print(img)
        im = Image.open(img) 
        print(im.size)
        im = crp_px_per(im ,px,per )
            if bool(im):
                im = im.save(os.path.join(dest_folder,file_name)) 


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scr_folder',default = 'G:\EPAi\epai_session11\modified_images', help='source folder ')
    parser.add_argument('--dest_folder',default = 'new' , help='destination folder ')
    parser.add_argument('--crop_px',default = 0 , help='No of pixel ')
    parser.add_argument('--crp_p',default = 0 , help='percentage of pixel')
    args = parser.parse_args()
    crop(scr_folder = args.scr_folder, dest_folder = args.dest_folder, px = args.crp_px, per = args.crp_p)