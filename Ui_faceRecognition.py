import face_recognition
import cv2
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_Lock import *
from Ui_start import *
from Ui_exit import *
from Ui_faceRecognition import *
import main

class Ui_faceRecognition(object):
    def setupUi(self, faceRecognition):
        faceRecognition.setObjectName("faceRecognition")
        faceRecognition.resize(211, 334)
        self.centralwidget = QtWidgets.QWidget(faceRecognition)
        self.centralwidget.setObjectName("centralwidget")
        self.wcamFButton = QtWidgets.QPushButton(self.centralwidget)
        self.wcamFButton.setGeometry(QtCore.QRect(20, 80, 171, 23))
        self.wcamFButton.setObjectName("wcamFButton")
        self.picFButton = QtWidgets.QPushButton(self.centralwidget)
        self.picFButton.setGeometry(QtCore.QRect(20, 120, 171, 23))
        self.picFButton.setObjectName("picFButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(20, 160, 171, 23))
        self.backButton.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 91, 20))
        self.label_2.setObjectName("label_2")
        faceRecognition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(faceRecognition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 211, 21))
        self.menubar.setObjectName("menubar")
        faceRecognition.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(faceRecognition)
        self.statusbar.setObjectName("statusbar")
        faceRecognition.setStatusBar(self.statusbar)

        self.retranslateUi(faceRecognition)
        self.wcamFButton.clicked.connect(self.frwFunction)
        self.picFButton.clicked.connect(self.frpFunction)
        self.backButton.clicked.connect(self.closeFace)
        QtCore.QMetaObject.connectSlotsByName(faceRecognition)

    def frwFunction(self):
        video_capture = cv2.VideoCapture(0)

        pooriya_image = face_recognition.load_image_file("03.jpg")
        pooriya_face_encoding = face_recognition.face_encodings(pooriya_image)[0]


        # Create arrays of known face encodings and their names
        known_face_encodings = [
            pooriya_face_encoding
        ]
        known_face_names = [
            "Pooriya"
        ]

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Only process every other frame of video to save time
            if process_this_frame:
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]

                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    face_names.append(name)

            process_this_frame = not process_this_frame

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

    def frpFunction(self):
        main.faceRecognition.close()
        main.result.show()

    def closeFace(self):
        main.faceRecognition.close()
        main.start.show()

    def retranslateUi(self, faceRecognition):
        _translate = QtCore.QCoreApplication.translate
        faceRecognition.setWindowTitle(_translate("faceRecognition", "MainWindow"))
        self.wcamFButton.setText(_translate("faceRecognition", "با استفاده از وب کم"))
        self.picFButton.setText(_translate("faceRecognition", "با استفاده از تصویر"))
        self.backButton.setText(_translate("faceRecognition", "بازگشت به منو"))
        self.label_2.setText(_translate("faceRecognition", "تشخیص چهره"))