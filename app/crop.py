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
    # print("inside crp_px",left, top, right, bottom)
    
    if right < width and bottom < height and left >0 and top > 0 :
        im1 = crop_image(im,left, top, right, bottom)
        print(im1.size)
        return im1
    else:
        print("out of bounds")
        return(None)
    
def crp_per(im,per):
    print(f"per {per}")
    width, height = im.size
    right = (width//2)+((width*(per/100))/2) #; print(f"{width//2})+(({width}*({per}//100))//2") 
    left = (width//2)-((width*(per/100))/2)
    top = (height//2)-((height*(per/100))/2)
    bottom = (height//2)+((height*(per/100))/2)
    print(left, top, right, bottom)
    im1 = crop_image(im,left, top, right, bottom)
    print(im1.size)
    return im1

def crp_px_per(im ,px = None,per = None ):
    if bool(px):
        im = crp_px(im,int(px))
    if bool(per):
        print(f"per {per}")
        im = crp_per(im,int(per))
    return im


def crop(scr_folder,dest_folder ,px = None,per = None):
    print(f"per {per}")
    create_dir(dest_folder)
    img_files = []
    for ext in ['jpg','JPG','JPEG','jpeg','png','PNG']:
        im_files = glob.glob(os.path.join(scr_folder,'*.'+ext))
        img_files += im_files

    for img in img_files:
        # print(img)
        file_name = img.split('\\')[-1]
        im = Image.open(img) 
        # print(im.size)
        im1 = crp_px_per(im ,px,per )
        if bool(im1):
            fn = os.path.join(dest_folder,file_name)
            # print(fn)
            im2 = im1.save(fn) 


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scr_folder',default = 'images', help='source folder')
    parser.add_argument('--dest_folder',default = 'new' , help='destination folder ')
    parser.add_argument('--crop_px',default = 0 , help='No of pixel ')
    parser.add_argument('--crp_p',default = 0 , help='percentage of pixel')
    args = parser.parse_args()
    crop(scr_folder = args.scr_folder, dest_folder = args.dest_folder, px = args.crp_px, per = args.crp_p)