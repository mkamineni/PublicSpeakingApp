import os
import cv2
import scipy.misc
import numpy
import requests

def evaluate_focus(video):
	cap = cv2.VideoCapture(video)

	off_center_counter=0
	last_off_center=0
	counter=0

	while(cap.isOpened()):
	    counter+=1
	    ## Read Image
	    ret, image = cap.read()
	    ## Convert to 1 channel only grayscale image
	    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	    ## CLAHE Equalization
	    cl1 = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	    clahe = cl1.apply(gray)
	    ## medianBlur the image to remove noise
	    blur = cv2.medianBlur(clahe, 7)
	    locations=get_irises_location(blur)

	    locations_y = sorted(locations, key=lambda x: x[1])
	    minimum=locations_y[-1][1]-locations_y[0][1]
	    min_index=-1

	    for ind in range(len(locations)-1):
	    	difference=abs(locations_y[ind][1]-locations_y[ind+1][1])
	    	if difference<=minimum:
	    		min_index=ind
	    		minimum=difference

	    for ind in [min_index, min_index+1]:
	        # draw the outer circle
	        circle=numpy.array(locations_y[ind])
	        cv2.circle(image,(circle[0],circle[1]),5,[0,255,0],2)
	        # draw the center of the circle
	        cv2.circle(image,(circle[0],circle[1]),2,(0,0,255),3)

	    scipy.misc.imsave('detected circles '+str(counter)+'.jpg', image)
	    off_center=get_off_center(locations_y[min_index], locations_y[min_index+1], 'detected circles '+str(counter)+'.jpg')
	    if off_center>0 and last_off_center<0 or off_center<0 and last_off_center>0 and abs(last_off_center-off_center)>30:
	    	off_center_counter+=1
	    elif abs(last_off_center-off_center)>50:
	    	off_center_counter+=1
	    last_off_center=off_center 
	    os.remove('detected circles '+str(counter)+'.jpg')

	cap.release()

	return off_center_counter

def get_irises_location(frame_gray):
    eye_cascade = cv2.CascadeClassifier('C:/Users/mkami/Anaconda3/Lib/site-packages/cv2/data/haarcascade_eye.xml')
    eyes = eye_cascade.detectMultiScale(frame_gray, 1.3, 10)  # if not empty - eyes detected
    irises = []

    for (ex, ey, ew, eh) in eyes:
        iris_w = int(ex + float(ew / 2))
        iris_h = int(ey + float(eh / 2))
        irises.append([numpy.float32(iris_w), numpy.float32(iris_h)])

    return numpy.array(irises)

def get_off_center(point1, point2, image):
	params = (
	    ('version', '2018-03-19'),
	)

	files= {'media': (image, open(image, 'rb'), 'jpg')}
	response = requests.post('https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces', files=files, 
		params=params, auth=('apikey', 'Aw5ZZ5ZHQPbUxqwueLo9afcUeFJIjEjLe5woFSt2Uztb')).json()
	loc=response["images"][0]["faces"][0]["face_location"]
	avg=loc["left"]+loc["width"]/2
	return (point1[1]+point2[1])/2-avg

video='vlog.mov'
process_video(video)
