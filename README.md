# Face_Detector_101
A face detector API that will help you detect faces from webcam feed or image

![image](.github/me.png) <-----> ![detected](.github/me-detected.png) 

### Its real easy
I guarentee you that this will be your most pleasent face detector


# Usage

1. go into the src folder and then into the `detection_from_images` folder or `detection_from_webcam` folder. then copy the file in the folder and paste it into the required directory

2. import the `FaceDetection101.py` file in a python file you want to work in

3. Now, import the only function in the file that might be any one of the one below according to the file that is in your directory

```python
faceDetection101.detect_faces_from_webcam(webcam_index=0, window_title='Faces In Video', box_colour=(0, 255, 0), line_thickness=2)
```

or 
```python
face_Detection101.detect_faces_from_image(image, box_colour=(0, 255, 0), line_thickness=2, window_title='faces in image', save=False, saving_filename=None)
```


### Customization

there are a lot of ways you can customisze this code line changing the parameters of the function 

> webcam_index (detect faces from different webcams)

> box_colour (change the colour of the rectangle around the face)

> line_thickness (change the thickenss of the lines of rectangle around the face)

> window_title (change the title of the window shown)

> save and saving filename (detection_from_image only) (save the file by setting the parameter `save=True` and provide the saving filename) 

#### box_colour 

the box_colour changes the colour of the rectangle around the face. the values is a Tuple and the tuple values **will not be in RGB** they are in BGR format.
so if green is `(0, 255, 0` in RGB
so green in BGR in `(255, 0, 0)`


thanks for reading. please communicate if you made something with it, I would be very happy 😊
