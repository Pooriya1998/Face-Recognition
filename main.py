import face_recognition
import cv2
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
import PIL.Image
import PIL.ImageDraw
import jdatetime
from Ui_Lock import *
from Ui_start import *
from Ui_exit import *
from Ui_faceRecognition import *
from Ui_result import *
from Ui_MainWindow import *
from Ui_FaceMakeup import *



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Lock = QtWidgets.QMainWindow()
    uiL = Ui_Lock()
    uiL.setupUi(Lock)
    Lock.show()
    start = QtWidgets.QMainWindow()
    uiStart = Ui_start()
    uiStart.setupUi(start)
    exit = QtWidgets.QMainWindow()
    uiExit = Ui_exit()
    uiExit.setupUi(exit)
    faceRecognition = QtWidgets.QMainWindow()
    uifR = Ui_faceRecognition()
    uifR.setupUi(faceRecognition)
    result = QtWidgets.QMainWindow()
    uiResult = Ui_result()
    uiResult.setupUi(result)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    FaceMakeup = QtWidgets.QMainWindow()
    ui1 = Ui_FaceMakeup()
    ui1.setupUi(FaceMakeup)
    sys.exit(app.exec())