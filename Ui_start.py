import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
import jdatetime
from Ui_Lock import *
import main

class Ui_start(object):
    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(212, 334)
        self.centralwidget = QtWidgets.QWidget(start)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 111, 20))
        self.label.setObjectName("label")
        self.timeB = QtWidgets.QTextBrowser(self.centralwidget)
        self.timeB.setGeometry(QtCore.QRect(20, 240, 171, 61))
        self.timeB.setObjectName("timeB")
        self.faceRButton = QtWidgets.QPushButton(self.centralwidget)
        self.faceRButton.setGeometry(QtCore.QRect(20, 80, 171, 23))
        self.faceRButton.setObjectName("faceRButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 120, 171, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setGeometry(QtCore.QRect(20, 200, 171, 23))
        self.exitbutton.setObjectName("exitbutton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 160, 171, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        start.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(start)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 212, 21))
        self.menubar.setObjectName("menubar")
        start.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(start)
        self.statusbar.setObjectName("statusbar")
        start.setStatusBar(self.statusbar)

        self.retranslateUi(start)
        self.timeW()
        self.faceRButton.clicked.connect(self.startFR)
        self.pushButton_2.clicked.connect(self.findFace)
        self.pushButton_4.clicked.connect(self.frm)
        self.exitbutton.clicked.connect(self.closeStart)
        QtCore.QMetaObject.connectSlotsByName(start)


    def timeW(self):
        self.timeB.append("زمان ورود کاربر")
        self.timeB.append(" ")
        self.timeB.append(str(jdatetime.datetime.today()))

    def startFR(self):
        main.faceRecognition.show()
        main.start.close()


    def findFace(self):
        main.MainWindow.show()
        main.start.close()


    def frm(self):
        main.FaceMakeup.show()
        main.start.close()

    def closeStart(self):
        exit.show()




    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "MainWindow"))
        self.label.setText(_translate("start", "نرم افزار تشخیص چهره"))
        self.faceRButton.setText(_translate("start", "تشخیص چهره"))
        self.pushButton_2.setText(_translate("start", "تشخیص حضور افراد در تصویر"))
        self.exitbutton.setText(_translate("start", "خروج"))
        self.pushButton_4.setText(_translate("start", "رنگ آمیزی اجزای چهره افراد"))
