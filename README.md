# Talaash #

## Talaash - with you, every step of the way. ##
### Powered by *machine learning*, *neural networks* and dlib's *state-of-the-art face recognition* technology ### 
* A face recognition desktop application built to find missing people. <br />
* The app aims to recognize faces through pictures, recordings and live stream videos and match them with a missing people's database. If a match occurs, the details of the person are flashed on screen and the family can be contacted for further communication. <br />

## Prerequisites ##
Make sure to install all the required libraries <br />
* Python version 3.3+ 
* pip install opencv-python
* pip install os
* pip install imutils
* pip install pillow
* pip install tkinter
* pip install numpy
* dlib can be installed on MacOS and Linus using the following documentation : https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf
* dlib can be installed on Windows 10 by typing pip install 'dlib-19.22.99-cp310-cp310-win_amd64.whl' (file added in the repository)
* pip install face_recognition

## Installation ##
* git clone https://github.com/ishitagupta2702/Talaash-FaceRecognition-Application
* cd ../path/to/the/file
* python start.py

## Navigating through the app ##

### Homepage ###
This is the landing page of the application. Users are provided with 4 functionalities which they can choose one by one. 

![talash](https://user-images.githubusercontent.com/79853573/170890341-3f11cad9-4e95-4f39-98f6-40608c9b59ac.png)

### Report a Missing Person ###
In case someone is missing, you can file a report by entering the details of the missing person along with their picture. This gets added to the database which is then used for facial recognition. 

![2](https://user-images.githubusercontent.com/79853573/170890247-7a3f3f7e-92e8-4dd8-b011-1802555216cc.png)

### Photo Match ###
Users can select a picture which is then passed through the face recognition model and the matching miss people entries are displayed in the table. 

![3](https://user-images.githubusercontent.com/79853573/170890293-03bc8047-6e89-4387-9271-da1084776bf9.png)

### Face Recognition in Live Video Surveillance ###
Faces are scanned and recognised through live streams and CCTV footage and the recognised people are flashed on screen with their details. 

![4](https://user-images.githubusercontent.com/79853573/170890300-1e200e8b-8fc8-40a1-a822-99de2c729d69.png)


