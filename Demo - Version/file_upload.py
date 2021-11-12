# import requests
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
# import os
# from tkinter import *
# from tkinter.messagebox import *
# from PIL import Image, ImageTk  # module to put ////////////////////image in tkinter
# import PIL
# import pickle
# import tkinter as tk
# from tkinter import messagebox
# import time
# from slide_show import slide_show
# from slide_show_zoomIn import slide_show_zoomIn
# from slide_show_zoomOut import slide_show_zoomOut
# from add_text_anim import add_text_anim
# from add_text_anim_videos import add_text_anim_videos
# from datetime import datetime
# import os
#from video_tool import video_tool
import cx_Oracle
# import imageio
import flask
# from flask import request, jsonify, send_file
import random
from datetime import datetime
import os
from moviepy.editor import *

#from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

from flask import Flask, jsonify, request
import json



app = flask.Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/user/Desktop/Demo - Version/upload_video'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['mp4', 'mp3', 'mov'])
video_file_name = None
video_file_name=[]



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def character_count(input_string):
    count = 0
    for c in input_string:
        if c.isspace() != True:
            count = count + 1
    return count

# def video_length(filename):
#     load_uploaded_video = os.path.join(UPLOAD_FOLDER, filename)
#     picture = VideoFileClip(load_uploaded_video, audio=True)
#     picture_length = int(picture.duration)
#     print(picture_length)
#     return picture_length


@app.route('/<string:STORE_ID>/video-file-upload', methods=['POST'])
def upload_file(STORE_ID):
    if request.method == 'POST' and 'video_files[]' in request.files:
        video_file_name.clear()
        print(request.files)
        files = request.files.getlist('video_files[]')
        # picture = VideoFileClip(files[0], audio=True)



        # print(files[0])
        # picture = VideoFileClip(files[0], audio=True)
        # print(picture.duration)
       # print(int(upload_video_path.duration))

        errors = {}
        success = False
        for file in files:
            if file and allowed_file(file.filename):
                date = datetime.now().strftime("%f_%p")
                file.filename = file.filename.replace(file.filename, STORE_ID + '-' + date + '.mp4' or '.mov')
                print(file.filename)
                #  global images_name_array
                video_file_name.append(file.filename)
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                success = True
        video = video_file_name

        return jsonify({'video_file': video})

    elif request.method == 'POST' and "text" in str(request.get_data()):
        content = flask.request.json#request.get_json()
        #content=json.dumps(content["texts"])
        dict_value_1=content["texts"][0]
        dict_value_1_1=dict_value_1['text']
        limit_1=character_count(dict_value_1_1)


        dict_value_2=content["texts"][1]
        dict_value_2_2=dict_value_2['text']
        limit_2=character_count(dict_value_2_2)

        if limit_1 < 6 and limit_2 < 6:
            return (content)
        else:
            return jsonify({"message": "character limit exceeded you can add atleast 100 characters"})


        # for i in content:
        #     contents.append(i['text'])#use for loop


@app.route('/<string:STORE_ID>/<string:BRANCH_ID>/upload', methods=['POST'])
def create_video(STORE_ID,BRANCH_ID):
    data = request.get_json()
    if 'video_file' in data:
        # data['images_files'] not in data
        video=str(data['video_file'])
        video_name=video.strip(" ['  '] ")
        images= None
        print(video)
        print(type(video))
        print('------------------------------------------------')
    else:
        return jsonify({"message":"no video file"})


    texts=[]
    for i in data['texts']:
        print(i)
        text=i['text'].split() #change the data type in db

        #text=text.strip("[ ]")

        # #text=str(texts)
      #  text=text.replace(" [' ', ' ']", " ' ', ' '")
        #print(text)
        texts.append(text)

    texts=str(texts)
    print(texts)
    print(type(texts))
    print('------------------------------------------------')

    merchant_id=str(STORE_ID)
    branch_id=str(BRANCH_ID)

    random_number= random.randint(3,10000 )
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H:%M:%S")
    random_number=str(random_number)
    dt_string=str(dt_string)
    video_id =random_number + '-' + dt_string
    print(video_id)
    print(type(video_id))

    status = "Pending"


    try:
        connection = cx_Oracle.connect("admin/Faiqalifarooqui12@eshop.cbp5pk0tdqap.us-east-2.rds.amazonaws.com:1521/orcl")
    except Exception as err:
        print("Error While Creating Connection to DB,Something went wrong try again!!")
        resp = jsonify({'message': 'Something Went Wrong!!'})
        resp.status_code = 400
        return resp
    else:
        try:
            rows = [(video_id,merchant_id,branch_id,video,texts,status)]
            print(rows)
            cursor = connection.cursor()
            cursor.executemany("""INSERT INTO DEMO_VERSION_1(VIDEO_ID,STORE_ID,BRANCH_ID,VIDEO,USER_TEXT,STATUS)VALUES (:1,:2,:3,:4,:5,:6)""", rows) #change TEXTS_USER
            connection.commit()
            # cursor.execute("SELECT VIDEO_ID FROM VIDEO_DATA WHERE IMAGES=:idbv ",images)
            # r= cursor.fetchone()
            # print(r)
        except Exception as err:
            print('Error While Inserting The Data, Something Went Wrong Try Again!')
            resp = jsonify({'message': 'Error While Inserting The Data, Something Went Wrong Try Again!!'})
            resp.status_code = 400
            return resp
        else:
            print("Insert Completed")
            resp = jsonify({'message':"your video is in progress",'video id': video_id,'video name':video_name })
            resp.status_code = 201
            return resp
    finally:
        cursor.close()
        connection.close()





if __name__ == '__main__':
    # Start a webserver
    app.run(port=5000)