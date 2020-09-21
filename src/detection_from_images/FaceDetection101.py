'''
Made By : Harsh Pandey (AkIonSight)
Contact : akionsight@gmail.com
Github Profile : https://github.com/akionsight
License : MIT
'''

import cv2

def detect_faces_from_image(image, box_colour=(0, 255, 0), line_thickness=2, window_title='faces in image', save=False, saving_filename=None):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')## loading cascade

    img = cv2.imread(image) ## reading image
    print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ## TO IMPROVE ACCURACY

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for x, y, w, h in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), box_colour, line_thickness)


    cv2.imshow(window_title, img)

    cv2.waitKey(0)
    if save:
        if saving_filename == None:
            raise ValueError('if save is set to True, filename must be provided')
        else:
            cv2.imwrite(saving_filename, img)
        
    

# detect_faces_from_image('me.png', save=True)

