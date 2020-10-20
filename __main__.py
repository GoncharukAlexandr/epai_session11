import glob
from PIL import Image
import os 
import argparse
from common_utils import *
from prop_resize import *
from crop import *


def all_aug(im , res_p , res_w ,res_h ,crp_px,crp_p):
    # if bool(res_p):
    #     im = prop_resize_img(im,res_p)
    # if bool(w_per) or bool(h_per):
    #     im = wh_prop_resize_img(im,percentage,w_per,h_per)
    if bool(w_per) or bool(h_per) or bool(res_p):
        im = wh_prop_resize_img(im,res_p , res_w ,res_h)  
    if 


    pass

def main():
