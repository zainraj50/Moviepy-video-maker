#import modules

# from moviepy.editor import ImageClip, concatenate
# import moviepy.video.fx.all as vfx

# from skimage import transform
# import numpy as np


# from natsort import natsorted
# import glob

# from moviepy.editor import *
# import moviepy.editor as mp
# import pandas as pd
# import numpy as np
# from sklearn.metrics import confusion_matrix
# from sklearn.naive_bayes import MultinomialNB
# from tkinter import *
# import joblib
import os
# from tkinter import *
# from tkinter.messagebox import *
# from PIL import Image, ImageTk  #module to put ////////////////////image in tkinter
# import PIL
# import pickle
# import tkinter as tk
# from tkinter import messagebox
# import time

from slide_show import slide_show
# from slide_show_zoomIn import slide_show_zoomIn
# from slide_show_zoomOut import slide_show_zoomOut
from add_text_anim import add_text_anim
# from add_text_anim_videos import add_text_anim_videos




#x=["'4c52d840bf2648f4909d9a7ea44f09ef.351962_PM.mp4'", "'4c52d840bf2648f4909d9a7ea44f09ef.400526_PM.mp3'", "'4c52d840bf2648f4909d9a7ea44f09ef.456303_PM.png'", "'hello', 'world'", 'Rated Best Item 2', 'Voucher and promotional discount you avail 3791.35']
#lst=["['4c52d840bf2648f4909d9a7ea44f09ef.178164_AM.mp4']", "['4c52d840bf2648f4909d9a7ea44f09ef.709492_AM.mp3']", "['4c52d840bf2648f4909d9a7ea44f09ef.962751_AM.png']", "[['hello'], ['world']]", 'Voucher and promotional discount you avail 3791.35', 'Saved By Discount 3783.8']
#lst=["['4c52d840bf2648f4909d9a7ea44f09ef.722385_AM.png', '4c52d840bf2648f4909d9a7ea44f09ef.739463_AM.png', '4c52d840bf2648f4909d9a7ea44f09ef.741722_AM.png']", "['4c52d840bf2648f4909d9a7ea44f09ef.709492_AM.mp3']", "['4c52d840bf2648f4909d9a7ea44f09ef.962751_AM.png']", "[['hello'], ['world']]", 'Saved By Discount 3783.8', 'Rated Best Item 2']
#merchant_id='4c52d840bf2648f4909d9a7ea44f09ef'
#lst=["['4c52d840bf2648f4909d9a7ea44f09ef.178164_AM.mp4']", "['4c52d840bf2648f4909d9a7ea44f09ef.709492_AM.mp3']", "['4c52d840bf2648f4909d9a7ea44f09ef.962751_AM.png']", "[['hello'], ['world']]", 'Sum of the Gross Price 12155.07', 'Voucher and promotional discount you avail 3791.35']

#img_lst=["4c52d840bf2648f4909d9a7ea44f09ef.722385_AM.png', '4c52d840bf2648f4909d9a7ea44f09ef.739463_AM.png', '4c52d840bf2648f4909d9a7ea44f09ef.741722_AM.png", '4c52d840bf2648f4909d9a7ea44f09ef.709492_AM.mp3', '4c52d840bf2648f4909d9a7ea44f09ef.962751_AM.png', "hello'], ['world", 'Total Items You Bought 12', 'Days Since Last Order 5']

# for i,j in enumerate(lst):
#     if i == 3:
#         a,b=j.split()
#         a=a.strip("'],")    #use this when adding text
#
#         b=b.strip("['")


#print(a)
#print(b)
def video_tool(merchant_id,lst=[]):
    new_lst=[]
    for list in lst:
        new_lst.append(list.strip(" ['  '] ']['"))
        #print(new_lst[0])

    audio_path=r"C:\Users\user\Downloads\AI Video Engine - Copy\upload_audio"
    audio_path=os.path.join(audio_path, new_lst[1])
        #print(audio_path)
    logo_path=r"C:\Users\user\Downloads\AI Video Engine - Copy\upload_logo"
    logo_path=os.path.join(logo_path, new_lst[2])

    if new_lst[0].endswith(('.mp4','.mov','.wmv','.avi')):
        for i, j in enumerate(new_lst):
            if i == 3:
                a, b = j.split()
                a = a.strip("'],")  # use this when adding text
                b = b.strip("['")

        first_path = r"C:\Users\user\Downloads\AI Video Engine - Copy\upload_video"
        first_path = os.path.join(first_path, new_lst[0])
        add_text_anim(first_path,logo_path,audio_path,new_lst[-1],new_lst[-2],a,b,merchant_id)
        print("video is Ready")
        return "video is ready"

    else:
        lst_images=[]
        lst=new_lst[0].split()
        for i in lst:
            data=i.strip(" '," )
            first_path = r"C:\Users\user\Downloads\AI Video Engine - Copy\uploads"
            first_path = os.path.join(first_path, data)
            lst_images.append(first_path)

        slide_show(merchant_id,lst_images)
        for i, j in enumerate(new_lst):
            if i == 3:
                a, b = j.split()
                a = a.strip("'],")  # use this when adding text
                b = b.strip("['")

        temp_video_path = r"C:\Users\user\Downloads\AI Video Engine - Copy\saved_slide_show"
        temp_video_path = os.path.join(temp_video_path, merchant_id + '.mp4')
        add_text_anim(temp_video_path, logo_path, audio_path, new_lst[-1], new_lst[-2], a, b,merchant_id)

        return "video is ready"


#video_tool(merchant_id,lst)

    #print(lst_images)
#     first_path = r"C:\Users\user\Downloads\AI Video Engine - Copy\uploads"
#     first_path = os.path.join(first_path, lst[0])
#     slide_show(first_path)
# #        time.sleep(360)
#     add_text_anim(first_path,logo_path,audio_path,lst[-1],lst[-2],a,b)
#     print("video is Ready")
        # except:
        #     print("Something Went Wrong!, please report the error so we can fixed it!")



#image_to_video(r'C:\Users\user\Downloads\AI Video Engine - Copy\Test1.mp4', r"C:\Users\user\Downloads\Towards Headlines\Towards Headlines-logo\profile.png",r'C:\Users\user\Downloads\Towards Headlines\Alex-Production.mp3',
              # 'Api Text','Api Text','no one but every one!', 'd')



#r'C:\Users\user\Downloads\Towards Headlines\Test1.mp4'
#r"C:\Users\user\Downloads\Towards Headlines\Towards Headlines-logo\profile.png"
#r'C:\Users\user\Downloads\Towards Headlines\Alex-Production.mp3'
