import cv2
import numpy as np

def process_video(video):
	cap = cv2.VideoCapture(video)

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
	    ## Detect Circles
	    #circles = cv2.HoughCircles(blur ,cv2.HOUGH_GRADIENT,1,20,
	    #                            param1=50,param2=30,minRadius=7,maxRadius=21)
	    circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,2,100,
                            param1=50,param2=30,minRadius=8,maxRadius=11)

	    if circles!=[]:
	        circles = np.uint16(np.around(circles)).astype("int")

	    for circle in circles[0,:]:
	        # draw the outer circle
	        circle=np.array(circle)
	        cv2.circle(image,(circle[0],circle[1]),circle[2],[0,255,0],2)
	        # draw the center of the circle
	        cv2.circle(image,(circle[0],circle[1]),2,(0,0,255),3)

	    cv2.imwrite('detected circles '+str(counter)+'.jpg',image)

	cap.release()

	return video

video='vlog.mov'
process_video(video)