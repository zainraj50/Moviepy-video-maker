# #!/usr/bin/env python
# # coding: utf-8
#
# # # WITH CUSTOMER_ID
#
# # In[1]:
#
#
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
# import seaborn as sns
# import numpy as np
# import cx_Oracle
# import imageio
# import flask
# from flask import request, jsonify
# import random
#
#
#
# #Define Flask MicroFrameWork
#
#
# app =flask.Flask(__name__)
#
# #############################The first title page to test API, not needed now#######################################
# # Display a welcome message on the 'home' page
# # @app.route('/')
# # def index():
# #     return "Welcome to the demo app"
#
# #############################The first title page to test API, not needed now#######################################
#
#
#
# # Show the username for a given id
#                                                 #give customer id like below in URL
# @app.route('/CUSTOMER_ID/<string:CUSTOMER_ID>') #http://127.0.0.1:5000/CUSTOMER_ID/8591f329347a4dbb8c832cd5239d8327
# def show_username(CUSTOMER_ID):
#     try:
#         l=[] #empty list to store iterated values.
#         ############################ Established Connection to Oracle DataBase ###############################################
#         connection = cx_Oracle.connect("admin/Faiqalifarooqui12@eshop.cbp5pk0tdqap.us-east-2.rds.amazonaws.com:1521/orcl")
#         cursor = connection.cursor()
#
#         ###The Provided Customer ID in the URL will be add in the query in :idbv, so that only filterred query return####
#         cursor.execute("SELECT * FROM AI_VIDEO_MESSAGE WHERE CUSTOMER_ID = :idbv", [CUSTOMER_ID])
#         r = cursor.fetchone() #it will fetch the first row as tupple where customer id is matched.
#         #     print(r)
#         data=r[2:] #The first two COLUMNS contains BRANCH_ID & CUSTOMER_ID so we slice data.
#
#
#         #####Now we iterate over data tupple according to index and only take those values which are not equal to 0 and append in list
#         for i,var in enumerate(data):
#             if i==0 and var!=0:
#                 l.append('The Successfull orders'+ ' ' +str(var))
#             elif i==1 and var!=0:
#                 l.append('Total Items You Bought'+ ' ' +str(var))
#             elif i==2 and var!=0:
#                 l.append('Voucher and promotional discount you avail'+ ' ' +str(var))
#             elif i==3 and var!=0:
#                 l.append('Sum of the Gross Price'+ ' ' +str(var))
#             elif i==4 and var!=0:
#                 l.append('Saved By Discount'+ ' ' +str(var))
#             elif i==5 and var!=0:
#                 l.append('Rated Best Item'+ ' ' +str(var))
#             elif i==6 and var!=0:
#                 l.append('Days Since Last Order'+ ' ' +str(var))
#
#         for i in range(2):
#             output=random.sample(l,2) #This will return two unique random string from a list.
#
#         return jsonify(output) #this will return 1 random value in response as JSON.
#
#     except Exception as  e:
#         print("ERROR: ", e, '\n')
#
#         return (abort(400))
#
#
# # Initialization is done once at startup time
# #
# if __name__ == '__main__':
#     # Start a webserver
#     app.run(port=5000)


# # WITH BRANCH_ID & CUSTOMER_ID

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np
import cx_Oracle
import imageio
import flask
from flask import request, jsonify, send_file
import random
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
import time
from slide_show import slide_show
from add_text_anim import add_text_anim
from add_text_anim_videos import add_text_anim_videos


def image_to_video(file=r'C:\Users\user\Downloads\Towards Headlines\Test1.mp4',logo=r"C:\Users\user\Downloads\Towards Headlines\Towards Headlines-logo\profile.png",audio=r'C:\Users\user\Downloads\Towards Headlines\Alex-Production.mp3',text_1='zain',text_2='11',heading_text1='no text provided',heading_text2='no text provided'):
    if file.endswith(('.mp4','.mov','.wmv','.avi')):
        add_text_anim_videos(file,logo,audio,text_1,text_2,heading_text1,heading_text2)
        print("video is Ready")

    else:
        slide_show(file)
#        time.sleep(360)
        add_text_anim(r'C:\Users\user\Downloads\AI Video Engine\Test1.mp4',logo,audio,text_1,text_2,heading_text1,heading_text2)
        print("video is Ready")
        # except:
        #     print("Something Went Wrong!, please report the error so we can fixed it!")

#Define Flask MicroFrameWork


app =flask.Flask(__name__)

#############################The first title page to test API, not needed now#######################################
# Display a welcome message on the 'home' page
# @app.route('/')
# def index():
#     return "Welcome to the demo app"

#############################The first title page to test API, not needed now#######################################



# Show the username for a given id
                                                                             #give BRANHC_ID & customer id like below in URL
@app.route('/BRANCH_ID/<string:BRANCH_ID>/CUSTOMER_ID/<string:CUSTOMER_ID>') #http://127.0.0.1:5000/BRANCH_ID/4c52d840bf2648f4909d9a7ea44f09ef/CUSTOMER_ID/8591f329347a4dbb8c832cd5239d8327
def show_username(BRANCH_ID,CUSTOMER_ID):
    try:
        l=[] #empty list to store iterated values.    
        ############################ Established Connection to Oracle DataBase ###############################################
        connection = cx_Oracle.connect("admin/Faiqalifarooqui12@eshop.cbp5pk0tdqap.us-east-2.rds.amazonaws.com:1521/orcl")
        cursor = connection.cursor()
        
        ###The Provided BRANCH_ID & Customer ID in the URL will be add in the query in :idbv, so that only filterred query return####
        cursor.execute("SELECT * FROM AI_VIDEO_MESSAGE WHERE BRANCH_ID= :idbv AND CUSTOMER_ID = :idbv", [BRANCH_ID,CUSTOMER_ID])
        r = cursor.fetchone() #it will fetch the first row as tupple where BRANCH_ID & customer id is matched.
        #     print(r)
        data=r[2:] #The first two COLUMNS contains BRANCH_ID & CUSTOMER_ID so we slice data.
        
        
        #####Now we iterate over data tupple according to index and only take those values which are not equal to 0 and append in list
        for i,var in enumerate(data):
            if i==0 and var!=0:
                l.append('The Successfull orders'+ ' ' +str(var))
            elif i==1 and var!=0:
                l.append('Total Items You Bought'+ ' ' +str(var))
            elif i==2 and var!=0:
                l.append('Voucher and promotional discount you avail'+ ' ' +str(var))
            elif i==3 and var!=0:
                l.append('Sum of the Gross Price'+ ' ' +str(var))
            elif i==4 and var!=0:
                l.append('Saved By Discount'+ ' ' +str(var))
            elif i==5 and var!=0:
                l.append('Rated Best Item'+ ' ' +str(var))
            elif i==6 and var!=0:
                l.append('Days Since Last Order'+ ' ' +str(var))
                
        for i in range(2):
            output=random.sample(l,2) #This will return two unique random string from a list.
            return output #this will return 1 random value in response as JSON.
    
    except Exception as  e:
        print("ERROR: ", e, '\n')
    else:
        return (abort(400))


# Initialization is done once at startup time
#
if __name__ == '__main__':
    # Start a webserver
    app.run(port=5000)


# In[ ]:




