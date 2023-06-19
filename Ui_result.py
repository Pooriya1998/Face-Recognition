import face_recognition
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_Lock import *
from Ui_start import *
from Ui_exit import *
from Ui_faceRecognition import *
import main


class Ui_result(object):
    def setupUi(self, result):
        result.setObjectName("result")
        result.resize(640, 394)
        self.centralwidget = QtWidgets.QWidget(result)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 200, 621, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(230, 110, 171, 23))
        self.backButton.setObjectName("backButton")
        self.frButton = QtWidgets.QPushButton(self.centralwidget)
        self.frButton.setGeometry(QtCore.QRect(230, 80, 171, 23))
        self.frButton.setObjectName("frButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 50, 291, 16))
        self.label.setObjectName("label")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 170, 621, 20))
        self.input.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 150, 291, 16))
        self.label_2.setObjectName("label_2")
        result.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(result)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        result.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(result)
        self.statusbar.setObjectName("statusbar")
        result.setStatusBar(self.statusbar)

        self.retranslateUi(result)
        self.frButton.clicked.connect(self.faceR)
        self.backButton.clicked.connect(self.backF)
        QtCore.QMetaObject.connectSlotsByName(result)

    def faceR(self):
        image_pooriya = face_recognition.load_image_file("03.jpg")

        pooriya = face_recognition.face_encodings(image_pooriya)[0]

        known_face_encodings = [
            pooriya,
        ]

        a = self.input.text()
        unknown_image = face_recognition.load_image_file(a)
        unknown_face_encodings = face_recognition.face_encodings(unknown_image)

        for unknown_face_encoding in unknown_face_encodings:
            results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)

            name = "unknown"

            if results[0]:
                name = "Pooriya Rahimzadeh"

            self.textBrowser.append(name)

    def backF(self):
        main.result.close()
        main.faceRecognition.show()


    def retranslateUi(self, result):
        _translate = QtCore.QCoreApplication.translate
        result.setWindowTitle(_translate("result", "MainWindow"))
        self.backButton.setText(_translate("result", "بازگشت به منو"))
        self.frButton.setText(_translate("result", "تشخیص چهره"))
        self.label.setText(_translate("result", "تشخیص چهره با استفاده از تصویر"))
        self.label_2.setText(_translate("result", "آدرس تصویر صورت را وارد کنید"))
