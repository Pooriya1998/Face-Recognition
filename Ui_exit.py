import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_Lock import *
from Ui_start import *
import main

class Ui_exit(object):
    def setupUi(self, exit):
        exit.setObjectName("exit")
        exit.resize(389, 150)
        self.centralwidget = QtWidgets.QWidget(exit)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 231, 20))
        self.label.setObjectName("label")
        self.yesButton = QtWidgets.QPushButton(self.centralwidget)
        self.yesButton.setGeometry(QtCore.QRect(210, 80, 101, 23))
        self.yesButton.setObjectName("yesButton")
        self.noButton = QtWidgets.QPushButton(self.centralwidget)
        self.noButton.setGeometry(QtCore.QRect(70, 80, 101, 23))
        self.noButton.setObjectName("noButton")
        exit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(exit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 389, 21))
        self.menubar.setObjectName("menubar")
        exit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(exit)
        self.statusbar.setObjectName("statusbar")
        exit.setStatusBar(self.statusbar)

        self.retranslateUi(exit)
        self.yesButton.clicked.connect(self.closeExit)
        self.noButton.clicked.connect(exit.close)
        QtCore.QMetaObject.connectSlotsByName(exit)

    def closeExit(self):
        exit.close()
        main.start.close()
        main.Lock.close()


    def retranslateUi(self, exit):
        _translate = QtCore.QCoreApplication.translate
        exit.setWindowTitle(_translate("exit", "MainWindow"))
        self.label.setText(_translate("exit", "آیا مطمئن هستید که می خواهید برنامه را ببندید؟"))
        self.yesButton.setText(_translate("exit", "بلی"))
        self.noButton.setText(_translate("exit", "خیر"))
