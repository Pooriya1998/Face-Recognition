import face_recognition
import cv2
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
import main

class Ui_Lock(object):
    def setupUi(self, Lock):
        Lock.setObjectName("Lock")
        Lock.resize(504, 207)
        self.centralwidget = QtWidgets.QWidget(Lock)
        self.centralwidget.setObjectName("centralwidget")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(280, 110, 171, 23))
        self.openButton.setObjectName("openButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(60, 110, 171, 23))
        self.exitButton.setObjectName("exitButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 441, 20))
        self.label_7.setObjectName("label_7")
        self.disp = QtWidgets.QTextBrowser(self.centralwidget)
        self.disp.setGeometry(QtCore.QRect(60, 150, 391, 43))
        self.disp.setObjectName("disp")
        Lock.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Lock)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 21))
        self.menubar.setObjectName("menubar")
        Lock.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Lock)
        self.statusbar.setObjectName("statusbar")
        Lock.setStatusBar(self.statusbar)

        self.retranslateUi(Lock)
        self.openButton.clicked.connect(self.openLock)
        self.exitButton.clicked.connect(self.exitLock)
        QtCore.QMetaObject.connectSlotsByName(Lock)


    def openLock(self):

        video_capture = cv2.VideoCapture(0)

        person_image = face_recognition.load_image_file("03.jpg")
        person_face_encoding = face_recognition.face_encodings(person_image)[0]

        known_face_encodings = [
            person_face_encoding
        ]
        known_face_names = [
            "Pooriya Rahimzadeh"
        ]

        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        c = 0

        while True:
            ret, frame = video_capture.read()

            if process_this_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                rgb_small_frame = small_frame[:, :, ::-1]

                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "unknown"

                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    face_names.append(name)

                    print("Face detected -- {}".format(face_names))

            process_this_frame = not process_this_frame
            print("Face detected -- {}".format(face_names))

            if list(face_names) == ['Pooriya Rahimzadeh']:
                main.start.show()
                main.Lock.close()
                break
            elif list(face_names) == ['unknown']:
                c += 1
                self.disp.clear()
                self.disp.append('شما نمی‌توانید وارد شوید ')
                print('شما نمی‌توانید وارد شوید ')
                if c == 5 :
                    break

            for (top, right, bottom, left), name in zip(face_locations, face_names):

                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q') :
                break

        video_capture.release()
        cv2.destroyAllWindows()


    def exitLock(self):
        exit.show()

    def retranslateUi(self, Lock):
        _translate = QtCore.QCoreApplication.translate
        Lock.setWindowTitle(_translate("Lock", "MainWindow"))
        self.openButton.setText(_translate("Lock", "ورود به نرم افزار"))
        self.exitButton.setText(_translate("Lock", "خروج"))
        self.label_7.setText(_translate("Lock","لطفا برای ورود  به نرم افزار روبروی دوربین ایستاده سپس دکمه ورود به نرم افزار را فشار دهید"))
