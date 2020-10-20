import glob
from PIL import Image
from common_utils import *
import os 



def prop_resize_img(img,percentage):
    percentage = int(percentage)
    print(percentage)
    width, height = img.size  
    width = width *(percentage / 100)
    height = height *(percentage / 100)

    img = resize(img,int(height),int(width))
    return img


def wh_resize_img(img,w_per,h_per):
    width, height = img.size  
    if bool(w_per):
        width = width *(w_per / 100)
    if bool(h_per):
        height = height *(h_per / 100)
    img = resize(img,int(height),int(width))
    return img

def wh_prop_resize_img(img,percentage,w_per,h_per):
    percentage = float(percentage)
    width, height = img.size  
    if bool(percentage):
        img = prop_resize_img(img,percentage)
    elif bool(w_per) or bool(h_per) :
        img = wh_resize_img(img,w_per,h_per)
    return img

def propation_resize_dir(scr_folder,dest_folder , percentage,w_per,h_per):
    create_dir(dest_folder)
    w_per = int(w_per)
    h_per = int(h_per)
    percentage = int(percentage)
    img_files = []
    for ext in ['jpg','JPG','JPEG','jpeg','png','PNG']:
        im_files = glob.glob(os.path.join(scr_folder,'*.'+ext))
        img_files += im_files
    for img in img_files:
        im1 = Image.open(img) 
        print('actual',im1.size)
        im2 = wh_prop_resize_img(im1,percentage,w_per,h_per)
        file_name = (img.split('\\')[-1])
        im3 = im2.save(os.path.join(dest_folder,file_name)) 
        print('resized',im2.size)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scr_folder',default = 'G:\EPAi\epai_session11\modified_images', help='source folder ')
    parser.add_argument('--dest_folder',default = 'new' , help='destination folder ')
    parser.add_argument('--res_p',default = 0 , help='percentage ')
    parser.add_argument('--res_w',default = 0 , help='res_w ')
    parser.add_argument('--res_h',default = 0 , help='res_h ')
    args = parser.parse_args()
    print(args)
    propation_resize_dir(scr_folder = args.scr_folder,dest_folder = args.dest_folder , percentage = args.res_p,w_per = args.res_w,h_per = args.res_h)