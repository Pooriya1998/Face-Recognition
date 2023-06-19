import face_recognition
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
import PIL.Image
import PIL.ImageDraw
from Ui_Lock import *
from Ui_start import *
from Ui_exit import *
from Ui_faceRecognition import *
import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 326)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 621, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 210, 621, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.picButton = QtWidgets.QPushButton(self.centralwidget)
        self.picButton.setGeometry(QtCore.QRect(190, 250, 111, 23))
        self.picButton.setObjectName("picButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(340, 250, 111, 23))
        self.backButton.setObjectName("backButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.picButton.clicked.connect(self.facePic)
        self.backButton.clicked.connect(self.backF)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def facePic(self):
        image = face_recognition.load_image_file(self.lineEdit.text())
        face_locations = face_recognition.face_locations(image)
        numberOfFace = len(face_locations)
        self.textBrowser.append(str(numberOfFace))

        pil_image = PIL.Image.fromarray(image)
        for face_location in face_locations:
            top, right, bottom, left = face_location
            draw = PIL.ImageDraw.Draw(pil_image)
            draw.rectangle([left, top, right, bottom], outline="red")

        pil_image.show()

        image_pooriya = face_recognition.load_image_file("03.jpg")
        image_parsar = face_recognition.load_image_file("01.jpg")
        image_farbod = face_recognition.load_image_file("02.jpg")

        pooriya = face_recognition.face_encodings(image_pooriya)[0]
        
        known_face_encodings = [
            pooriya
        ]

        unknown_face_encodings = face_recognition.face_encodings(image)

        for unknown_face_encoding in unknown_face_encodings:
            results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)

            name = "unknown"

            if results[0]:
                name = "Pooriya"

            self.textBrowser.append(name)


    def backF(self):
        main.MainWindow.close()
        main.start.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.picButton.setText(_translate("MainWindow", "بررسی تصویر"))
        self.backButton.setText(_translate("MainWindow", "بازگشت به منو"))
