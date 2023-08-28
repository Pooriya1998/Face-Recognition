import face_recognition
import cv2
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
import jdatetime
import PIL.Image
import PIL.ImageDraw

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

        person_image = face_recognition.load_image_file("04.jpg")
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

                rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

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
                start.show()
                Lock.close()
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
        faceRecognition.show()
        start.close()


    def findFace(self):
        MainWindow.show()
        start.close()


    def frm(self):
        FaceMakeup.show()
        start.close()

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
        start.close()
        Lock.close()


    def retranslateUi(self, exit):
        _translate = QtCore.QCoreApplication.translate
        exit.setWindowTitle(_translate("exit", "MainWindow"))
        self.label.setText(_translate("exit", "آیا مطمئن هستید که می خواهید برنامه را ببندید؟"))
        self.yesButton.setText(_translate("exit", "بلی"))
        self.noButton.setText(_translate("exit", "خیر"))

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

        farbod_image = face_recognition.load_image_file("02.jpg")
        farbod_face_encoding = face_recognition.face_encodings(farbod_image)[0]

        # Create arrays of known face encodings and their names
        known_face_encodings = [
            pooriya_face_encoding,
            farbod_face_encoding
        ]
        known_face_names = [
            "Pooriya",
            "Farbod Pil"
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
                rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

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
        faceRecognition.close()
        result.show()

    def closeFace(self):
        faceRecognition.close()
        start.show()

    def retranslateUi(self, faceRecognition):
        _translate = QtCore.QCoreApplication.translate
        faceRecognition.setWindowTitle(_translate("faceRecognition", "MainWindow"))
        self.wcamFButton.setText(_translate("faceRecognition", "با استفاده از وب کم"))
        self.picFButton.setText(_translate("faceRecognition", "با استفاده از تصویر"))
        self.backButton.setText(_translate("faceRecognition", "بازگشت به منو"))
        self.label_2.setText(_translate("faceRecognition", "تشخیص چهره"))

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
        image_farbod = face_recognition.load_image_file("02.jpg")
        image_parsar = face_recognition.load_image_file("01.jpg")

        pooriya = face_recognition.face_encodings(image_pooriya)[0]
        farbod = face_recognition.face_encodings(image_farbod)[0]
        parsar = face_recognition.face_encodings(image_parsar)[0]

        known_face_encodings = [
            pooriya,
            farbod,
            parsar
        ]

        a = self.input.text()
        unknown_image = face_recognition.load_image_file(a)
        unknown_face_encodings = face_recognition.face_encodings(unknown_image)

        for unknown_face_encoding in unknown_face_encodings:
            results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)

            name = "unknown"

            if results[0]:
                name = "Pooriya Rahimzadeh"
            elif results[1]:
                name = "farbod khalili"
            elif results[2]:
                name = "Parsa Rahimzadeh"


            self.textBrowser.append(name)

    def backF(self):
        result.close()
        faceRecognition.show()


    def retranslateUi(self, result):
        _translate = QtCore.QCoreApplication.translate
        result.setWindowTitle(_translate("result", "MainWindow"))
        self.backButton.setText(_translate("result", "بازگشت به منو"))
        self.frButton.setText(_translate("result", "تشخیص چهره"))
        self.label.setText(_translate("result", "تشخیص چهره با استفاده از تصویر"))
        self.label_2.setText(_translate("result", "آدرس تصویر صورت را وارد کنید"))

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
        parsar = face_recognition.face_encodings(image_parsar)[0]
        farbod = face_recognition.face_encodings(image_farbod)[0]

        known_face_encodings = [
            pooriya,
            parsar,
            farbod
        ]

        unknown_face_encodings = face_recognition.face_encodings(image)

        for unknown_face_encoding in unknown_face_encodings:
            results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)

            name = "unknown"

            if results[0]:
                name = "Pooriya"
            elif results[1]:
                name = "Parsa Rahimzadeh"
            elif results[2]:
                name = "farbod"

            self.textBrowser.append(name)


    def backF(self):
        MainWindow.close()
        start.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.picButton.setText(_translate("MainWindow", "بررسی تصویر"))
        self.backButton.setText(_translate("MainWindow", "بازگشت به منو"))

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
        start.show()
        FaceMakeup.close()
    def retranslateUi(self, FaceMakeup):
        _translate = QtCore.QCoreApplication.translate
        FaceMakeup.setWindowTitle(_translate("FaceMakeup", "MainWindow"))
        self.pushButton.setText(_translate("FaceMakeup", "بازگشت به منو"))
        self.pushButton_2.setText(_translate("FaceMakeup", "انجام عملیات"))
        self.label.setText(_translate("FaceMakeup", "آدرس تصویر"))
        self.label_2.setText(_translate("FaceMakeup", "رنگ چشم ها"))
        self.label_3.setText(_translate("FaceMakeup", "رنگ ابرو ها"))
        self.label_4.setText(_translate("FaceMakeup", "رنگ لب ها"))

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
