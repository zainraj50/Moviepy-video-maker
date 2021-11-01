from moviepy.editor import ImageClip, concatenate
import moviepy.video.fx.all as vfx

from skimage import transform
import numpy as np


from natsort import natsorted
import glob

from moviepy.editor import *
import moviepy.editor as mp
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from tkinter import *
import joblib
import os
from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk  #module to put ////////////////////image in tkinter
import PIL
import pickle
import tkinter as tk
from tkinter import messagebox

# def zoomIn(t):
#   return 1 + 0.1 * t
duration = 10
screensize = (1920, 1080) #2k common high defination video often reffered as 1080p


# def resize_func(t):
#     if t < 12:
#         return 1 + 0.02 * (duration - t)
#
#     #     elif 4 <= t <= 6:
#     #         return 1 + 0.02*4  # Stay.
#     else:
#         return 1 + 0.02 * t  # Zoom-in.# 6 < t
#         # Zoom-out.


def slide_show(merchant_id,images=None):
    if images is None:
        images = []
    ####################### Saving images in a list to calculate number of images ##########################
    # no_of_images=[]
    # for image in natsorted(
    #         glob.glob(path + '/**.png')):  # bug here only handle png images find another way to iterate
    #     no_of_images.append(image)


    print('Total Images Are:',len(images))
    ###################### END #######################################


    img_clip = []
    duration = 30//len(images)
    # for image in natsorted(
    #         glob.glob(images)):  # bug here only handle png images find another way to iterate
    for image in images:
        # print(image)
        x = ImageClip(image).resize(screensize).set_position(('right', 'left')).set_duration(
            duration).set_fps(25)
#
        img_clip.append(x)  # 1.7+0*t
        # print(img_clip)

    video = concatenate(img_clip, method='compose').margin(40)
    # video.resize( (460,720) ) # New resolution: (460,720)
    # video.resize(2) # width and heigth multiplied by 0.6
    # video.resize(width=8000) # height computed automatically.
    # video.resize(lambda t : 1+0.02*t) # slow swelling of the clip
    saved_path = r"C:\Users\user\Downloads\AI Video Engine - Copy\saved_slide_show"
    saved_path = os.path.join(saved_path, merchant_id)

    return video.write_videofile(saved_path +".mp4")

#slide_show(r'C:\Users\user\Downloads\Towards Headlines\afghanistan')