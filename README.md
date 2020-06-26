# Face_Detector_101
A face detector API that will help you detect faces from webcam feed 

### Its real easy
I guarentee you that this will be your most pleasent face detector


# Usage

## Cloning the repository

clone the repository will the following command
```git clone https://github.com/akionsight/Face_Detector_101.git```

![cloneing](https://github.com/akionsight/Face-Detector-101/blob/master/github/cloneing.gif)

## after that import the file as

```python 
from Face-Detector-101/src import FaceDetection101.py
```

## How to use 
after writing 
```python 
from Face-Detector-101/src import FaceDetection101
```

then you can write 

```python 
FaceDetection101.detect_faces_from_webcam()
```
and you get you being recognized

### Customization

there are a lot of ways you can customisze this code line changing the parameters of the function 

> webcam_index (detect faces from multiple webcams)

> box_colour (change the colour of the rectangle around the face)

> line_thickness (change the thickenss of the lines of rectangle around the face)

> cascade (now you can recognize thing such as eyes, nose, ears, whole body, lower body, upper body etc)

#### webcam_index

the webcam index is a integer value. the default is 0 but if another webcam is installed the index will be 1 etc. 

#### box_colour 

the box_colour changes the colour of the rectangle around the face. the values is a Tuple and the tuple values **will not be in RGB** they are in BGR format.
so if green is `(0, 255, 0` in RGB
so green in BGR in `(255, 0, 0)`

#### line thickness
the line_thickness changes the thickenss of the lines of rectangle around the face. the default value is 2

#### cascade
the cascade or haarcascade can be changed. to view the list of all harcascades for ears, nose etc click [here](https://github.com/opencv/opencv/tree/master/data/haarcascades) and download the required cascade, you can also create you own cascade and use it here



thanks for reading. please tell if you made something with it I would be very happy 😊
