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


def add_text_anim(video_path,logo_path,audio_path,text_1,text_2,heading_text_1,heading_text_2,merchant_id):
    picture = VideoFileClip(video_path, audio=False).add_mask() #
    picture =picture.set_pos('center','center')
    durations = int(picture.duration)
    print("Video Length is:",durations)
    end_video = VideoFileClip(r'C:\Users\user\Downloads\Planckly Logo animation\Planckly logo.mp4')
    end_video = end_video.subclip(2)
    # end_video=end_video.resize( (1920, 1080) )
    end_video = end_video.set_pos('center', 'center').crossfadein(.6)

    w, h = moviesize = picture.size



    ######################## Logo #####################################
    logo = (mp.ImageClip(logo_path)
            .set_duration(picture.duration)
            .resize(height=200)  # if you need to resize...
            .margin(right=20, top=20, opacity=0)  # (optional) logo-border padding
            .set_pos(('right', 'top')))
    ####################### Logo ####################################

    ###################### heading Text ############################
    heading = TextClip(heading_text_1, fontsize=25, color='White')
    heading_col = heading.on_color(size=(heading.w + 120, heading.h + 130), color=(0,0,128), pos=('center', 'center'),col_opacity=(.5)) #changrd
    heading = heading_col.set_pos((w/6.5 , h  / 1.3)).set_duration(durations - 4).crossfadeout(.6)  ##put ((100,200))
    #################### heading Text ##############################


    ###################### heading Text 2 ############################
    heading1 = TextClip(heading_text_2, fontsize=25, color='White')
    heading_col1 = heading1.on_color(size=(heading.w + 100, heading.h + 8), color=(0,0,128), pos=('center', 'center'),col_opacity=(.5)) #changrd
    heading1 = heading_col1.set_pos((w / 1.6, h / 1.3)).set_duration(durations - 4).crossfadeout(.6)  ##put ((100,200)) #.set_pos((1700, 1100))
    #################### heading Text 2 ##############################

    textOne = text_1  # "First Line!"
    textTwo = text_2  # Second Caption!!!!"
    textThree = 'Thank You \n for being connected with us!!'  # "Third one!!!"




    texts = [textOne, textTwo, textThree]

    step = durations//3  # each 15 sec: 0, 15, 30
    # duration = 10
    t = 2
    txt_clips = []
    for text, i in zip(texts, range(0, 3)):
        # txt_clip = TextClip(text,fontsize = 40, color='white')
        txt_clip = TextClip(text, font='Amiri-regular', color='white', fontsize=50, stroke_width=1)
        txt_col = txt_clip.on_color(size=(txt_clip.w + 150, txt_clip.h + 280 ), color=(3, 200, 255), pos=('center', 'center'),
                                      col_opacity=.8) # color=( 43, 134, 230 )
        txt_col = txt_col.set_start(t)
        # txt_clip = txt_clip.set_pos('center').set_duration(duration)
        txt_mov = txt_col.set_pos(lambda t: (
        max(w / 3.4, int(-0.2 * w * t)),  # w*t*10 ye text slide jaldi move karwata hai, #for ticker remove -0.2
        max(h * 2 / 10, int(10 * t)))).set_duration(step).crossfadein(.6)  # 5*h/6 default , #i have changed h* 4/10 to h*2/10
        # for fixed ticker text used h*3/7,(-1*w*t) above

        txt_clips.append(txt_mov)
        t += step

    audio = AudioFileClip(audio_path).subclip(0, durations)

    video_with_new_audio = picture.set_audio(audio)

    final_video = CompositeVideoClip(
        [video_with_new_audio, logo, heading,heading1, txt_clips[0], txt_clips[1], txt_clips[2],end_video.set_start(durations)])##txt_clip[3] added


    saved_path = r"C:\Users\user\Downloads\AI Video Engine - Copy\ready_video"
    saved_path = os.path.join(saved_path, merchant_id)

    return final_video.write_videofile(saved_path +".mp4")

#add_text_anim(r'C:\Users\user\Downloads\Video sample\Video sample.mp4', r"C:\Users\user\Downloads\Towards Headlines\Towards Headlines-logo\profile.png",r'C:\Users\user\Downloads\Towards Headlines\Alex-Production.mp3',
 #              'The Successful Orders are 183','Vouchers and Promotional \n Discounts  you avail are  183','no one but every one!', 'no one but everyone!')
