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

class Ui_FaceMakeup(object):
    def setupUi(self, FaceMakeup):
        FaceMakeup.setObjectName("FaceMakeup")
        FaceMakeup.resize(640, 204)
        self.centralwidget = QtWidgets.QWidget(FaceMakeup)
        self.centralwidget.setObjectName("centralwidget")
        self.inputLine = QtWidgets.QLineEdit(self.centralwidget)
        self.inputLine.setGeometry(QtCore.QRect(10, 40, 611, 20))
        self.inputLine.setObjectName("inputLine")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 120, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 120, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(446, 20, 171, 21))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 71, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 100, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 100, 71, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 130, 113, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 130, 71, 21))
        self.label_4.setObjectName("label_4")
        FaceMakeup.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FaceMakeup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        FaceMakeup.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FaceMakeup)
        self.statusbar.setObjectName("statusbar")
        FaceMakeup.setStatusBar(self.statusbar)

        self.retranslateUi(FaceMakeup)
        self.pushButton_2.clicked.connect(self.frM)
        self.pushButton.clicked.connect(self.backF)
        QtCore.QMetaObject.connectSlotsByName(FaceMakeup)

    def frM(self):

        a = str(self.inputLine.text())
        b = str(self.lineEdit_2.text())
        c = str(self.lineEdit_3.text())
        e = str(self.lineEdit_4.text())
        image = face_recognition.load_image_file(a)

        # Find all facial features in all the faces in the image
        face_landmarks_list = face_recognition.face_landmarks(image)

        pil_image = PIL.Image.fromarray(image)
        for face_landmarks in face_landmarks_list:
            d = PIL.ImageDraw.Draw(pil_image, 'RGBA')

            # Make the eyebrows into a nightmare
            d.polygon(face_landmarks['left_eyebrow'], fill=c)
            d.polygon(face_landmarks['right_eyebrow'], fill=c)
            d.line(face_landmarks['left_eyebrow'], fill=c, width=5)
            d.line(face_landmarks['right_eyebrow'], fill=c, width=5)

            # Gloss the lips
            d.polygon(face_landmarks['top_lip'], fill=e)
            d.polygon(face_landmarks['bottom_lip'], fill=e)
            d.line(face_landmarks['top_lip'], fill=e, width=8)
            d.line(face_landmarks['bottom_lip'], fill=e, width=8)

            # Sparkle the eyes
            d.polygon(face_landmarks['left_eye'], fill=b)
            d.polygon(face_landmarks['right_eye'], fill=b)

            # Apply some eyeliner
            d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=b, width=6)
            d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=b, width=6)

            pil_image.show()
    def backF(self):
        main.start.show()
        main.FaceMakeup.close()
    def retranslateUi(self, FaceMakeup):
        _translate = QtCore.QCoreApplication.translate
        FaceMakeup.setWindowTitle(_translate("FaceMakeup", "MainWindow"))
        self.pushButton.setText(_translate("FaceMakeup", "بازگشت به منو"))
        self.pushButton_2.setText(_translate("FaceMakeup", "انجام عملیات"))
        self.label.setText(_translate("FaceMakeup", "آدرس تصویر"))
        self.label_2.setText(_translate("FaceMakeup", "رنگ چشم ها"))
        self.label_3.setText(_translate("FaceMakeup", "رنگ ابرو ها"))
        self.label_4.setText(_translate("FaceMakeup", "رنگ لب ها"))