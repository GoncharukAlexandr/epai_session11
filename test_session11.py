from __main__ import *
import glob
from PIL import Image
import os 
import argparse
from common_utils import *
from prop_resize import *
from crop import *
from j2p import *
from p2j import *


def test_j2p_1():
    scr_folder = 'images'
    dest_folder = 'jpg_png'
    jpg2png(scr_folder,dest_folder)
    all_act = glob.glob(os.path.join(scr_folder, '*.*'))
    counter_s = 0
    counter_d = 0
    for f in all_act:
        for e in ['jpg','JPG','JPEG','jpeg']:
            if e in f:
                counter_s +=1
    counter_d = len(glob.glob(os.path.join(dest_folder, '*.*')))

    assert counter_s == counter_d

def test_p2j_1():
    scr_folder = 'jpg_png'
    dest_folder = 'png_jpg'
    png2jpg(scr_folder,dest_folder)
    all_act = glob.glob(os.path.join(scr_folder, '*.*'))
    counter_s = 0
    counter_d = 0
    for f in all_act:
        for e in ["png","PNG"]:
            if e in f:
                counter_s +=1
    counter_d = len(glob.glob(os.path.join(dest_folder, '*.jpg')))

    assert counter_s == counter_d

def test_crop_px():
    crop(scr_folder = "images",dest_folder = "cpx",px =50,per = None)
    a_images = glob.glob("./images/*.*")
    o_images = glob.glob("./cpx/*.*")
    im1 = Image.open(o_images[0]) 
    im2 = Image.open(os.path.join("images",o_images[0].split("\\")[-1]) )
    assert im1.size[0] < im2.size[0]


def test_crop_per():
    crop(scr_folder = "images",dest_folder = "cper",px =None,per = 50)
    a_images = glob.glob("./images/*.*")
    o_images = glob.glob("./cper/*.*")
    im1 = Image.open(o_images[0]) 
    im2 = Image.open(os.path.join("images",o_images[0].split("\\")[-1]) )
    assert im1.size[0] < im2.size[0]

def test_res_p():
    propation_resize_dir(scr_folder = "images" ,dest_folder = 'res_p' , percentage = 20 ,w_per = 0,h_per = 0)
    a_images = glob.glob("./images/*.*")
    o_images = glob.glob("./res_p/*.*")
    im1 = Image.open(o_images[0]) 
    im2 = Image.open(os.path.join("images",o_images[0].split("\\")[-1]) )
    assert im1.size[0] < im2.size[0]

def test_res_w_per():
    propation_resize_dir(scr_folder = "images" ,dest_folder = 'w_per' , percentage = 0,w_per = 10,h_per = 0)
    a_images = glob.glob("./images/*.*")
    o_images = glob.glob("./w_per/*.*")
    im1 = Image.open(o_images[0]) 
    im2 = Image.open(os.path.join("images",o_images[0].split("\\")[-1]) )
    assert im1.size[1] < im2.size[1]

def test_res_h_per():
    propation_resize_dir(scr_folder = "images" ,dest_folder = 'h_per' , percentage = 0,w_per = 0,h_per = 30)
    a_images = glob.glob("./images/*.*")
    o_images = glob.glob("./h_per/*.*")
    im1 = Image.open(o_images[0]) 
    im2 = Image.open(os.path.join("./images",o_images[0].split("\\")[-1]) )
    assert im1.size[0] < im2.size[0]

# def test_error():
