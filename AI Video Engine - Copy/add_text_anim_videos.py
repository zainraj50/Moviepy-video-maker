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

from moviepy.editor import *


def add_text_anim_videos(video_path,logo_path,audio_path,text_1,text_2,heading_text_1,heading_text_2):
    picture = VideoFileClip(video_path, audio=False).subclip(0,30).add_mask()  #
    durations = int(picture.duration)
    print("Video Length is:",durations)

    ######################## Logo #####################################
    logo = (mp.ImageClip(logo_path)
            .set_duration(picture.duration)
            .resize(height=50)  # if you need to resize...
            .margin(right=20, top=20, opacity=0)  # (optional) logo-border padding
            .set_pos(('right', 'top')))
    ####################### Logo ####################################

    ###################### heading Text ############################
    heading = TextClip(heading_text_1, fontsize=50, color='White')
    heading_col = heading.on_color(size=(heading.w + 5, heading.h + 5), color=(69, 10, 51), pos=('center', 'center')) #changrd
    heading = heading_col.set_pos((80, 1100)).set_duration(durations - 4)  ##put ((100,200))
    #################### heading Text ##############################

    ###################### heading Text 2 ############################
    heading1 = TextClip(heading_text_2, fontsize=50, color='White')
    heading_col1 = heading1.on_color(size=(heading.w + 5, heading.h + 5), color=(69, 10, 51), pos=('center', 'center')) #changrd
    heading1 = heading_col1.set_pos((2050, 1100)).set_duration(durations - 4)  ##put ((100,200))
    #################### heading Text 2 ##############################

    textOne = text_1 # "First Line!"
    textTwo = text_2  # Second Caption!!!!"
    textThree = 'Thank You!!'  # "Third one!!!"


    w, h = moviesize = picture.size

    texts = [textOne, textTwo, textThree]

    step =  3    #durations//5  # each 15 sec: 0, 15, 30

    # duration = 10
    t = 20
    txt_clips = []
    for text, i in zip(texts, range(0, 3)):
        # txt_clip = TextClip(text,fontsize = 40, color='white')
        txt_clip = TextClip(text, font='Amiri-regular', color='white', fontsize=30, stroke_width=1)
        txt_col = txt_clip.on_color(size=(txt_clip.w + 55, txt_clip.h - 10), color=(0, 0, 255), pos=('center', 'center'),
                                    col_opacity=0.6)  # color=( 43, 134, 230 )
        txt_col = txt_col.set_start(t)
        # txt_clip = txt_clip.set_pos('center').set_duration(duration)
        txt_mov = txt_col.set_pos(lambda t: (
        max(w / 2.5, int(-0.2 * w * t)),  # w*t*10 ye text slide jaldi move karwata hai, #for ticker remove -0.2
        max(h * 4 / 10, int(10 * t)))).set_duration(step)  # 5*h/6 default ,
        # for fixed ticker text used h*3/7,(-1*w*t) above

        txt_clips.append(txt_mov)
        t += step

    audio = AudioFileClip(audio_path).subclip(0, durations)

    video_with_new_audio = picture.set_audio(audio)

    final_video = CompositeVideoClip(
        [video_with_new_audio, logo, heading,heading1, txt_clips[0], txt_clips[1], txt_clips[2]])  ##txt_clip[3] added
    return final_video.write_videofile("TEXT2.mp4")