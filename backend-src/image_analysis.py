import cv2
import httplib2
import PIL
import scipy.misc
import os
from time import sleep
from io import BytesIO

import requests
from PIL import Image
import numpy as np

def process_video(video_path):
    subscription_key = "24d68589f2f84295b86891153db557fb"
    assert subscription_key
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
    image_url = 'https://how-old.net/Images/faces2/main007.jpg'

    headers = {'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
        'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
    }

    vidcap = cv2.VideoCapture(video_path)
    length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    success,image = vidcap.read()
    
    emotion = {}
    smile = []

    count = 0
    interval = length//60
    
    while success and count<length:
        success,image = vidcap.read()
        print(count,interval,length)
        if count%interval == 0 :
            print('in')
            
            scipy.misc.imsave('outfile.jpg',image)

            with open("outfile.jpg",'rb') as f:
                a = f.read()

            response = requests.post(face_api_url, data=a, headers=headers, params=params)
            faces = response.json()
            os.remove("outfile.jpg")
            sleep(3)

            if faces!=[]:
                print(faces[0]["faceAttributes"]["smile"],faces[0]["faceAttributes"]["emotion"])
                for i in faces[0]["faceAttributes"]["emotion"]:
                    if i not in emotion:
                        emotion[i]=[faces[0]["faceAttributes"]["emotion"][i]]
                    else:
                        emotion[i].append(faces[0]["faceAttributes"]["emotion"][i])
                smile.append(faces[0]["faceAttributes"]["smile"])
        count += 1
    return smile, emotion

