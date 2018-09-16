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
import json
from watson_developer_cloud import VisualRecognitionV3



def process_video(video_path, key):
    subscription_key = key
    assert subscription_key
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
    image_url = 'https://how-old.net/Images/faces2/main007.jpg'
    visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    #url='https://gateway.watsonplatform.net/visual-recognition/api',
    iam_apikey='kBfzi5ljS1A6hqUViA4ijnSSbge-eMm_UpX_VC4llc-Z')

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
    posture = {}
    smile = []

    count = 0
    interval = length//60
    
    while success and count<length:
        success,image = vidcap.read()
        #print(count,interval,length)
        if count%interval == 0 :
            #print('in')
            
            scipy.misc.imsave('outfile.jpg',image)

            a = None

            with open("outfile.jpg",'rb') as f:
                classes = visual_recognition.classify(
                    images_file=f,
                    threshold='0',
                    classifier_ids=['DefaultCustomModel_138415036']).get_result()
                #print(json.dumps(classes, indent=2))
                a = classes["images"][0]["classifiers"][0]["classes"]
                for i,idict in enumerate(a):
                    if a[i]["class"] not in posture:
                        posture[a[i]["class"]] = [a[i]["score"]]
                    else:
                        posture[a[i]["class"]].append(a[i]["score"])
                f.seek(0)
                a = f.read()


            response = requests.post(face_api_url, data=a, headers=headers, params=params)
            faces = response.json()
            os.remove("outfile.jpg")
            sleep(3)
            #print(faces)
            if faces!=[] and 'error' not in faces:
                print(faces[0]["faceAttributes"]["smile"],faces[0]["faceAttributes"]["emotion"])
                for i in faces[0]["faceAttributes"]["emotion"]:
                    if i not in emotion:
                        emotion[i]=[faces[0]["faceAttributes"]["emotion"][i]]
                    else:
                        emotion[i].append(faces[0]["faceAttributes"]["emotion"][i])
                smile.append(faces[0]["faceAttributes"]["smile"])
        count += 1
    #print(smile, emotion, posture)
    return smile, emotion, posture

process_video(video_path='silence.mp4',key="24d68589f2f84295b86891153db557fb")