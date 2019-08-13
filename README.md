# Handling-pictures
face detection, face recognition, GAN


### Must import

1. dlib (19.17.0)
2. face-recognition (1.2.3)
3. face-recognition-models (0.3.0)
4. Pillow (6.1.0)
5. opencv-python(3.2.0)


### install manual

1. git clone https://github.com/davisking/dlib.git
2. cd dlib
3. mkdir build; cd build; cmake ..; cmake --build .
4. cd ..
5. python3 setup.py install
6. pip3 install face_recognition
7. python3 -m pip install Pillow
8. pip3 install opencv-python

## Function explain

### num_of_face.py

count the number of faces in the picture and return True if there is only one.

*input:
 
path of profile image

*output: 

1. Boolean_type True, coordinate of face
2. Boolean_type False