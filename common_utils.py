import glob
from PIL import Image
import os 
import argparse
from __main__ import *

def create_dir(dir):
    if os.path.exists(dir):
        pass
    else:
        os.mkdir(dir)

def change_extension(to_be_ext,ext_list,scr_folder,dest_folder ):
    img_files = []
    for ext in ext_list:
        im_files = glob.glob(os.path.join(scr_folder,'*.'+ext))
        img_files += im_files
    print(img_files)
    for img in img_files:
        # creating a image object (main image)  
        im1 = Image.open(img)   
        # if aug :
        #     im = all_aug(im , res_p , res_w ,res_h ,crp_px,crp_p)
        file_name = (img.split('\\')[-1]).split('.')[0]
        im1 = im1.save(os.path.join(dest_folder,file_name+'.'+to_be_ext))  

def resize(img,height,width):
    newsize = (int(height),int(width))
    print('newsize',newsize)
    img = img.resize(newsize) 
    return img

# def crop(img,x1,x2,y1,y2):
#     img = img[x1:x2,y1:y2]
#     return 

def crop_image(im,left, top, right, bottom):
    im1 = im.crop((left, top, right, bottom)) 
    return im1
