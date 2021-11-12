# from moviepy.editor import ImageClip, concatenate
# import moviepy.video.fx.all as vfx
#
# from skimage import transform
# import numpy as np
#
#
# from natsort import natsorted
# import glob
#
# from moviepy.editor import *
import moviepy.editor as mp
# import pandas as pd
# import numpy as np
# from sklearn.metrics import confusion_matrix
# from sklearn.naive_bayes import MultinomialNB
# from tkinter import *
# import joblib
# import os
# from tkinter import *
# from tkinter.messagebox import *
# from PIL import Image, ImageTk  #module to put ////////////////////image in tkinter
# import PIL
# import pickle
# import tkinter as tk
# from tkinter import messagebox

from moviepy.editor import *


def add_text_anim(video_path,text_1,text_2,heading_text_1,heading_text_2,merchant_id,logo_path=r'C:\Users\user\Desktop\Demo - Version\profile.png'):
    picture = VideoFileClip(video_path, audio=True).add_mask() #
    if picture.duration >= 30:
        picture=picture.subclip(0,30)
    else:
        pass
    picture = picture.resize(height=720)  # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
    picture =picture.set_pos('center','center')
    durations = int(picture.duration)
    print("Video Length is:",durations)
    end_video = VideoFileClip(r'C:\Users\user\Desktop\Demo - Version\Planckly Logo animation\Planckly logo.mp4')
    end_video = end_video.subclip(2)
    # end_video=end_video.resize( (1920, 1080) )
    end_video = end_video.set_pos('center', 'center').crossfadein(.6)

    w, h = moviesize = picture.size



    ######################## Logo #####################################
    logo = (mp.ImageClip(logo_path)
            .set_duration(picture.duration)
            .resize(height=100)  # if you need to resize...
            .margin(right=40, top=40, opacity=0)  # (optional) logo-border padding
            .set_pos(('right', 'top')))
    ####################### Logo ####################################

    ###################### heading Text ############################
    heading = TextClip(heading_text_1, fontsize=15, color='White')
    heading_col = heading.on_color(size=(heading.w + 70, heading.h + 70), color=(0,0,128), pos=('center', 'center'),col_opacity=(.5)) #changrd
    heading = heading_col.set_pos((w/6.5 , h  / 1.3)).set_duration(durations//2).crossfadeout(.6)  ##put ((100,200))
    #################### heading Text ##############################


    ###################### heading Text 2 ############################
    heading1 = TextClip(heading_text_2, fontsize=25, color='White')
    heading_col1 = heading1.on_color(size=(heading.w + 40, heading.h + 8), color=(0,0,128), pos=('center', 'center'),col_opacity=(.5)) #changrd
    heading1 = heading_col1.set_pos((w / 1.6, h / 1.3)).set_duration(durations//2).crossfadeout(.6)  ##put ((100,200)) #.set_pos((1700, 1100))
    #################### heading Text 2 ##############################

    textOne = text_1  # "First Line!"
    textTwo = text_2  # Second Caption!!!!"
    textThree = 'Thank You \n for being connected with us!!'  # "Third one!!!"




    texts = [textOne, textTwo, textThree]

    step = durations//3  # each 15 sec: 0, 15, 30
    # duration = 10
    t = 3
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

    # audio = AudioFileClip(audio_path).subclip(0, durations)
    #
    # video_with_new_audio = picture.set_audio(audio)

    final_video = CompositeVideoClip(
        [picture, logo, heading,heading1, txt_clips[0], txt_clips[1], txt_clips[2],end_video.set_start(durations)])##txt_clip[3] added


    saved_path = r"C:\Users\user\Desktop\Demo - Version\ready_video"
    saved_path = os.path.join(saved_path, merchant_id)

    return final_video.write_videofile(saved_path +".mp4")

# add_text_anim(r"C:\Users\user\Videos\Captures\meeting1.mp4", r"C:\Users\user\Downloads\Towards Headlines\Towards Headlines-logo\profile.png",
#               'The Successful Orders are 183','Vouchers and Promotional \n Discounts  you avail are  183','no one but every one!', 'no one but everyone!',"4c52d840bf2648f4909d9a7ea44f09ef")


# from moviepy.editor import ImageClip, concatenate
# import moviepy.video.fx.all as vfx
#
# from skimage import transform
# import numpy as np
#
#
# from natsort import natsorted
# import glob
#
# from moviepy.editor import *
# import moviepy.editor as mp
# #import pandas as pd
# #import numpy as np
# #from sklearn.metrics import confusion_matrix
# #from sklearn.naive_bayes import MultinomialNB
# #from tkinter import *
# import joblib
# import os
# #from tkinter import *
# #from tkinter.messagebox import *
# #from PIL import Image, ImageTk  #module to put ////////////////////image in tkinter
# #import PIL
# #import pickle
# #import tkinter as tk
# #from tkinter import messagebox
#
# from moviepy.editor import *

# def video_tool(merchant_id,video_path,logo_path):
#     picture = VideoFileClip(video_path, audio=True).subclip(0,30).add_mask()  #
#     picture_resized = picture.resize(height=720)  # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
#     durations = int(picture_resized.duration)
#     print("Video Length is:",durations)
#
#     ######################## Logo #####################################
#     logo = (mp.ImageClip(logo_path)
#             .set_duration(picture_resized.duration)
#             .resize(height=50)  # if you need to resize...
#             .margin(right=20, top=20, opacity=0)  # (optional) logo-border padding
#             .set_pos(('right', 'top')))
#     ####################### Logo ####################################
#
#     ###################### heading Text ############################
#     # heading = TextClip(heading_text_1, fontsize=50, color='White')
#     # heading_col = heading.on_color(size=(heading.w + 5, heading.h + 5), color=(69, 10, 51), pos=('center', 'center')) #changrd
#     # heading = heading_col.set_pos((80, 1100)).set_duration(durations - 4)  ##put ((100,200))
#     #################### heading Text ##############################
#
#     ###################### heading Text 2 ############################
#     # heading1 = TextClip(heading_text_2, fontsize=50, color='White')
#     # heading_col1 = heading1.on_color(size=(heading.w + 5, heading.h + 5), color=(69, 10, 51), pos=('center', 'center')) #changrd
#     # heading1 = heading_col1.set_pos((2050, 1100)).set_duration(durations - 4)  ##put ((100,200))
#     #################### heading Text 2 ##############################
#
#     # textOne = text_1 # "First Line!"
#     # textTwo = text_2  # Second Caption!!!!"
#     # textThree = 'Thank You!!'  # "Third one!!!"
#
#
#     w, h = moviesize = picture_resized.size
#
#     # texts = [textOne, textTwo, textThree]
#     #
#     # step =  3    #durations//5  # each 15 sec: 0, 15, 30
#     #
#     # # duration = 10
#     # t = 20
#     # txt_clips = []
#     # for text, i in zip(texts, range(0, 3)):
#     #     # txt_clip = TextClip(text,fontsize = 40, color='white')
#     #     txt_clip = TextClip(text, font='Amiri-regular', color='white', fontsize=30, stroke_width=1)
#     #     txt_col = txt_clip.on_color(size=(txt_clip.w + 55, txt_clip.h - 10), color=(0, 0, 255), pos=('center', 'center'),
#     #                                 col_opacity=0.6)  # color=( 43, 134, 230 )
#     #     txt_col = txt_col.set_start(t)
#     #     # txt_clip = txt_clip.set_pos('center').set_duration(duration)
#     #     txt_mov = txt_col.set_pos(lambda t: (
#     #     max(w / 2.5, int(-0.2 * w * t)),  # w*t*10 ye text slide jaldi move karwata hai, #for ticker remove -0.2
#     #     max(h * 4 / 10, int(10 * t)))).set_duration(step)  # 5*h/6 default ,
#     #     # for fixed ticker text used h*3/7,(-1*w*t) above
#     #
#     #     txt_clips.append(txt_mov)
#     #     t += step
#     #
#     # audio = AudioFileClip(audio_path).subclip(0, durations)
#     #
#     # video_with_new_audio = picture.set_audio(audio)
#     saved_path = r"C:\Users\user\Desktop\Demo - Version\ready_video"
#     saved_path = os.path.join(saved_path, merchant_id)
#
#     final_video = CompositeVideoClip(
#         [picture_resized, logo])  ##txt_clip[3] added
#     return final_video.write_videofile(saved_path +".mp4")

#add_text_anim_videos("4c52d840bf2648f4909d9a7ea44f09ef",r"C:\Users\user\Videos\Captures\meeting1.mp4",r"C:\Users\user\Downloads\Towards Headlines\Towards Headlines-logo\profile.png")

