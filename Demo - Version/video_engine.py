#import os
from video_tool import add_text_anim
import cx_Oracle
import random
import time
# from urllib.parse import urljoin
# from PIL import Image
# import requests
import requests
import os
from tqdm import tqdm
#from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))

def video_tool(merchant_id, video_id, customer_id,lst=[]):
    new_lst=[]
    for list in lst:
        new_lst.append(list.strip(" ['  '] ']['"))
    print(new_lst)


    #logo_path=r"C:\Users\user\Desktop\Demo - Version\logo.png"
    #logo_path=os.path.join(logo_path, new_lst[4])

    if new_lst[0].endswith(('.mp4','.mov','.wmv','.avi')):
        for i, j in enumerate(new_lst):
            if i == 2:
                a, b = j.split()
                a = a.strip("'],")  # use this when adding text
                b = b.strip("['")
                print(a)
                print(b)

        first_path = r"C:\Users\user\Desktop\Demo - Version\upload_video"
        first_path = os.path.join(first_path, new_lst[0])
        logo_path = r"C:\Users\user\Desktop\Demo - Version\logo-images"
        logo_path = os.path.join(logo_path, new_lst[1])
        add_text_anim(first_path,new_lst[-1],new_lst[-2],a,b,merchant_id,logo_path)#r"C:\Users\user\Downloads\Towards Headlines\Towards Headlines-logo\profile.png"
        connection = cx_Oracle.connect(
            "admin/Faiqalifarooqui12@eshop.cbp5pk0tdqap.us-east-2.rds.amazonaws.com:1521/orcl")
        cursor=connection.cursor()
        cursor.execute("UPDATE DEMO_VERSION_1 SET STATUS= 'Done' WHERE VIDEO_ID=:idbv AND STORE_ID = :idbv",
                        [video_id,merchant_id])
        connection.commit()

        print("video is Ready")

        return "video is ready"
    else:
        return "video format is not supported"


while True:
    connection = cx_Oracle.connect("admin/Faiqalifarooqui12@eshop.cbp5pk0tdqap.us-east-2.rds.amazonaws.com:1521/orcl")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()

    #cursor4 = connection.cursor()


    cursor1.execute("SELECT * FROM DEMO_VERSION_1 WHERE STATUS='Pending'")#"SELECT *  FROM FINAL_VIDEO_DATA_TABLE WHERE STATUS = 'Pending'")
    data_final=cursor1.fetchone()
    if data_final != None:
        print(data_final)
        video_id=data_final[0]
        merchant_id=data_final[1] #merchant_id = store_id
        video = data_final[2]
        user_text=data_final[3]
        status=data_final[4]
        branch_id=data_final[5]
        branch_id=str(branch_id)
        customer_id="8591f329347a4dbb8c832cd5239d8327"
        print("video id is:",video_id)
        print("Store id:",merchant_id)
        print("branch id:",branch_id)
        print("video:", video)
        print("user text: ",user_text)
        print("status:",status)
        print("------------------------------------------------------------------->")
        cursor3.execute("SELECT LOGO FROM STORES WHERE STORE_ID=:idbv",[merchant_id])
        logo_data=cursor3.fetchone()
        logo_data=logo_data[0]
        url=urljoin('https://images.planckly.com/file-uploads/store-images/',logo_data)#'https://ueshop.acledabank.com.kh/api/planckly-shopping-service/images/file-uploads/store-images/',logo_data)
        #im = Image.open(requests.get(url, stream=True).raw)
        download(url,
                 r"C:\Users\user\Desktop\Demo - Version\logo-images")

        print("------------------------------------------------------------------->")
        row=[merchant_id,customer_id]
        cursor2.execute("SELECT * FROM AI_VIDEO_MESSAGE WHERE STORE_ID= :idbv AND CUSTOMER_ID = :idbv",row)
        r = cursor2.fetchone()
        l=[]
        video_data_list=[]
        if r == None:
            ai_text_data_1='No AI data available for this user text 1'
            ai_text_data_2 = 'No AI data available for this user text 2'
            ai_text_data_3 = 'No AI data available for this user text 3'
            l.append(ai_text_data_1)
            l.append(ai_text_data_2)
            l.append(ai_text_data_3)
        else:
            ai_text_data = r[3:]
            for i, var in enumerate(ai_text_data):
                #print(i,var)
                if i == 0 and var != 0:
                    l.append('The Successfull orders' + ' ' + str(var))
                elif i == 1 and var != 0:
                    l.append('Total Items You Bought' + ' ' + str(var))
                elif i == 2 and var != 0:
                    l.append('Voucher and promotional discount you avail' + ' ' + str(var))
                elif i == 3 and var != 0:
                    l.append('Sum of the Gross Price' + ' ' + str(var))
                elif i == 4 and var != 0:
                    l.append('Saved By Discount' + ' ' + str(var))
                elif i == 5 and var != 0:
                    l.append('Rated Best Item' + ' ' + str(var))
                elif i == 6 and var != 0:
                    l.append('Days Since Last Order' + ' ' + str(var))

        output = random.sample(l, 2)
        #print(l)
        print(output)
        # for x in data_final:
        #     if x != None :
        #         x =x.strip("[' ']")
        #         x=x[1:-1]
        #         video_data_list.append(x)
        video_data_list.append(video)
        video_data_list.append(logo_data)
        video_data_list.append(user_text)
        video_data_list.append(output[0])
        video_data_list.append(output[1])
        print(video_data_list)
        #print(l)

        # new_lst=[]
        # for list in enumerate(video_data_list):
        #     new_lst.append(list.strip(" ['  '] ']['"))
        #     print(new_lst)
        video_tool(merchant_id,video_id, customer_id, video_data_list)


    else:
        print("There is no new video request video engine will be sleep for 30 seconds")
        message = "your video was already made"
        time.sleep(30)
        #return message
        print("-------------------------------------------------------------------->")
