import cv2
import os
def detect_faces_from_webcam(webcam_index=0, window_title='Faces In Video', cascade='haarcascade_frontalface_default.xml',box_colour=(0, 255, 0), line_thickness=2):
    face_cascade = cv2.CascadeClassifier(cascade)

    cap = cv2.VideoCapture(webcam_index)
    while True:
        _, img = cap.read()
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, 1)
        faces = face_cascade.detectMultiScale(grey, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), box_colour, line_thickness)

        cv2.imshow(window_title, img)
        k = cv2.waitKey(30)
        if k == 27:
            break

