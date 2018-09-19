# Pitch Perfect
Jessica Yin, Kaveri Nadhamuni, Shannen Wu, Meghana Kamineni

Pitch Perfect is a mobile app we built to give a user info and machine learning based personalised suggestions on public speaking! We're still working on the integration between back end and front end, but the individual parts are working.

You open the mobile app, Pitch Perfect, and position the phone so it is secured in front of you, roughly at eye level. Record a video of yourself speaking, making sure to try and look at the camera, work on your body language, and smile!

Finish the recording and your video will be analyzed. See your personalized feedback on:
  a) Body Language - Eye contact tracking, posture and gestures, facial emotion recognition.
  
  b) Audio - Tone analysis, pauses, filler words

Back End Features:
1) Eye Contact Tracking: We used CLAHE Equalization to identify the iris radii on the face. Then we used the Watson Vision Recognition API to find the offset distance between the center of the two irises and the center of the face bounding box. We recorded the time when the difference between these central points was greater than a threshold distance. We timed the durations of staying within the threshold (keeping consistent eye contact) and the durations of switching eye contact and presented these stats and recommendations for the user.

2) Facial Emotion Recognition:  We used the Microsoft Azure API to scan emotion of the user at certain frames of the input video and plot the varying expressions over the course of the speech.  We monitor the amount of time that the user was smiling as well.

3) Posture and Gestures: We trained a classifier with the IBM Watsom custom model framework based on confident and diffident hand gestures and postures. We classify the video frames accordingly with a probability score of 'confidence' or 'diffidence' between 0 and 1.

4) Filler Words: With the Rev API, we converted user speech to text and counted filler words, which we inform the user of.
5) Pauses and Tone analysis: We record the pace of speech and count the time between words at the end of punctuation to find the average pauses and advise the user on slowing down/speeding up. We used the IBM Watson Sentiment Analysis tool to monitor and inform the user of the tone of the speech.

Front End Features:
1) Record Video
2) Annotate text with filler words and pauses
3) Present tone and body language stats
